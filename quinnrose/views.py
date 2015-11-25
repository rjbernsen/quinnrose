import os
import glob
import logging
from django.views.generic import TemplateView
from django.shortcuts import render

from quinnrose.menus import menu
from quinnrose.home_page_info import home_page_info
from quinnrose.featurettes import featurettes
from quinnrose.config import CONFIG_CONTEXT

class BasePage(TemplateView):
    default_title = CONFIG_CONTEXT['full_site_name']
    
#     def __init__(self, template_name, *args, **kwargs):
#         
#         super().__init__(*args, **kwargs)
#         
    logging.info('line 16')
    def get_context_data(self, sub_title, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        context.update(CONFIG_CONTEXT)
        context['page_title'] = self._get_title(sub_title)
        context['menu'] = menu

        return context

    def _get_title(self, sub_title=None):
        
        if sub_title:
            page_title = '{} - {}'.format(self.default_title,sub_title)
        else:
            page_title = self.default_title
        
        return page_title
    
class HomePage(BasePage):
    template_name = 'home.html'
    page_sub_title = None
    
#     def __init__(self, *args, **kwargs):
#         
#         super().__init__(self.template_name, args, kwargs)
        

    def get_context_data(self, **kwargs):

        context = super().get_context_data(self.page_sub_title, **kwargs)

        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(root_dir, 'static', 'images') + '/carousel-*'
        carousel_images = [
            os.path.basename(p) for p in glob.glob(image_path)
        ]
    
        context['carousel_images'] = carousel_images
        context['home_page_info'] = home_page_info
        context['featurettes'] = featurettes

        return context

class About(BasePage):
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
        context = super().get_context_data(self.page_sub_title, **kwargs)

        section = context.get('section') or '1'
        
        self.template_name = 'about_{}.html'.format(self.sections[int(section)])
        
        return context
    
class Privacy(BasePage):
    template_name = 'privacy.html'
    page_sub_title = 'Privacy Policy'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(self.page_sub_title, **kwargs)
        return context
    
class Terms(BasePage):
    template_name = 'terms.html'
    page_sub_title = 'Terms and Conditions'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(self.page_sub_title, **kwargs)

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
    