import os
import glob
# import logging
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from quinnrose.menus import menu
from quinnrose.forms import ContactForm
from quinnrose.home_page_info import home_page_info
from quinnrose.featurettes import featurettes
from quinnrose.config import CONFIG_CONTEXT

class BasePage(object):
    default_title = CONFIG_CONTEXT['full_site_name']
    
    def init(self, extra_page_context={}):
        self.context = {
            'page_title': self._get_title(),
            'menu': menu,
        }
        
        self.context.update(extra_page_context)
        self.context.update(CONFIG_CONTEXT)
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.update(self.context)
        
        return context

    def _get_title(self):
        
        if self.page_sub_title:
            page_title = '{} - {}'.format(self.default_title,self.page_sub_title)
        else:
            page_title = self.default_title
        
        return page_title
    
class BaseTemplatePage(BasePage, TemplateView):
    """
    This is simply a base class for the purpose of
    multiple inheritance in the views.
    """
    pass

class BaseFormPage(BasePage, FormView):
    """
    This is simply a base class for the purpose of
    multiple inheritance in the views.
    """
    pass


class HomePage(BaseTemplatePage):
    template_name = 'home.html'
    page_sub_title = None
    
    def get_context_data(self, **kwargs):
        

        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(root_dir, 'static', 'images') + '/carousel-*'
        carousel_images = [
            os.path.basename(p) for p in glob.glob(image_path)
        ]
        
        more_page_context = {
            'carousel_images': carousel_images,
            'home_page_info': home_page_info,
            'featurettes': featurettes,
        }

        self.init(more_page_context)
    
        context = super().get_context_data(**kwargs)

        return context

class About(BaseTemplatePage):
    template_name = 'about.html'
    page_sub_title = 'About'

    section = None
    
    sections = [
        None,
        'the_site',
        'core_values',
        'mission_statement',
        'we_do',
        'we_dont'
    ]
    
    def get_context_data(self, **kwargs):
        
        self.init()
        
        context = super().get_context_data(**kwargs)

        section = context.get('section') or '1'
        
        self.template_name = 'about_{}.html'.format(self.sections[int(section)])
        
        return context

class ContactFormView(BaseFormPage):
    template_name = 'contact.html'
    page_sub_title = 'Contact Us'
    form_class = ContactForm
    success_url = '/contact/thanks'
    
    def get(self, request, *args, **kwargs):
    
        return super(ContactFormView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            # <process form cleaned data>
            pass #return HttpResponseRedirect('/success/')

        return render(request, self.success_url, {'form': form})
    
    def form_valid(self, form):
        from_email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        send_mail(
            subject='Subject',
            message=message,
            from_email=from_email,
            recipient_list=['a@b.com'],
        )
        return super(ContactFormView, self).form_valid(form)
            
    def get_context_data(self, **kwargs):
 
        self.init()
        
        context = super().get_context_data(**kwargs)
        return context

class Privacy(BaseTemplatePage):
    template_name = 'privacy.html'
    page_sub_title = 'Privacy Policy'

    def get_context_data(self, **kwargs):

        self.init()
        
        context = super().get_context_data(**kwargs)
        return context
    
class Terms(BaseTemplatePage):
    template_name = 'terms.html'
    page_sub_title = 'Terms and Conditions'

    def get_context_data(self, **kwargs):

        self.init()
        
        context = super().get_context_data(**kwargs)

        return context
    
# def home_page(request):
#     page_title = 'QuinnRose Talent Connection'
#     root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     image_path = os.path.join(root_dir, 'static', 'images') + '/carousel-*'
#     carousel_images = [
#         os.path.basename(p) for p in glob.glob(image_path)
#     ]
#     
#     context = {
#         'page_title': page_title,
#         'menu': menu,
#         'carousel_images': carousel_images,
#         'home_page_info': home_page_info,
#         'featurettes': featurettes,
#     }
#     
#     return render(request,'home.html', context)
# 
# def privacy(request):
# 
#     return render(request,'privacy.html')
    
# def new_list(request):
#     form = NewListForm(data=request.POST)
#     if form.is_valid():
#         list_ = form.save(owner=request.user)
#         return redirect(list_)
#     return render(request, 'home.html', {'form': form})
# 
# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     form = ExistingListItemForm(for_list=list_)
# 
#     if request.method == 'POST':
#         form = ExistingListItemForm(for_list=list_, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(list_)
#     return render(request,'list.html', {'list': list_, 'form': form})
# 
# def my_lists(request, email):
#     owner = User.objects.get(email=email)
#     return render(request, 'my_lists.html', {'owner': owner})
def error404(request):
    page_title = 'QuinnRose Talent Connection - Page Not Found!'

    context = {
        'page_title': page_title,
    }
    return render(request,'404.html', context)

if __name__ == '__main__':
    image_path = '../static/images/carousel-*'
    carousel_images = glob.glob(image_path)
    print(carousel_images)
    