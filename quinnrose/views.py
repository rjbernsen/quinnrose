import os
import glob
import logging
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import TemplateView, FormView
# from django.contrib.messages.views import SuccessMessageMixin

from quinnrose.menus import menu
from quinnrose.forms import SignInForm, ContactForm
from quinnrose.home_page_info import home_page_info
from quinnrose.featurettes import featurettes
from quinnrose.temp_data import HELP_DATA, SUBSCRIPTIONS_DATA
from quinnrose.config import CONFIG_CONTEXT, CONTACT_SUBJECT_EMAILS

class BasePage(object):
    default_title = CONFIG_CONTEXT['full_site_name']
    
    logger = logging.getLogger('quinnrose')

    def init(self, extra_page_context={}):
        self.context = {
            'page_title': self._get_title(),
            'page_header': self.page_sub_title,
            'menu': menu,
        }
        
        self.context.update(extra_page_context)
        self.context.update(CONFIG_CONTEXT)
        
    def get_context_data(self, **kwargs):
#         self.logger.info('Base kwargs = {}'.format(self.kwargs))
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
#         self.logger.info('context = {}'.format(context))
        context.update(self.context)
#         self.logger.info('context = {}'.format(context))
        context.update(self.kwargs)
#         self.logger.info('context = {}'.format(context))
        
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
    multiple inheritance in the template views.
    """

class BaseFormPage(BasePage, FormView):
    """
    This is simply a base class for the purpose of
    multiple inheritance in the form views.
    """

    def get_context_data(self, **kwargs):
 
        self.init()
        
        context = super().get_context_data(**kwargs)
        return context

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

class SignInFormView(BaseFormPage):
    template_name = 'signin_{}.html'
    page_sub_title = 'Sign In'
    form_class = SignInForm
    
    sub_titles = {
        'signin': 'Sign in',
        'register': 'Register'
    }
#     success_message = "Message was sent successfully"
#     success_url = '/contact/thanks'
    
    def get(self, request, *args, **kwargs):
    
        return super(SignInFormView, self).get(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
# 
#         form = self.form_class(request.POST)
#         
#         if form.is_valid():
# 
#             subject = CONTACT_SUBJECT_EMAILS[int(form.cleaned_data.get('subject'))][0]
#             from_email = form.cleaned_data.get('email')
#             recipient_list = ['rjbdevel@gmail.com'] #[CONTACT_SUBJECT_EMAILS[int(form.cleaned_data.get('subject'))][1]]
#             message = form.cleaned_data.get('message')
#             
#             try:
#                 sent_count = send_mail(
#                     subject=subject,
#                     from_email=from_email,
#                     recipient_list=recipient_list,
#                     message=message,
#                 )
# #                 raise SMTPAuthenticationError('asdf','asdf')
# #                 self.logger.info('sent_count = {}'.format(sent_count))
#                 if sent_count != 1:
# 
#                     messages.error(request, 'Could not send the message. Please try again later.')
#                     return render_to_response(
#                         self.template_name,
#                         context_instance=RequestContext(
#                             request,
#                             self.get_context_data(form=form)
#                         )
#                     )
#                     
#                 messages.success(request, self.success_message)
#             
#             except Exception as e:
#                 self.logger.info(e.__class__)
#                 self.logger.info(e)
#                 messages.error(request, 'Could not send the message. Please try again later.')
#             
#             return render_to_response(
#                 self.template_name,
#                 context_instance=RequestContext(
#                     request,
#                     self.get_context_data(form=self.form_class)
#                 )
#             )
#         
#         return self.get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        subtype = self.kwargs.get('subtype') or 'signin'
 
        self.page_sub_title = self.sub_titles[subtype]
        
        self.init()
        
        context = super().get_context_data(**kwargs)
        context['subtype'] = subtype

        self.template_name = self.template_name.format(subtype)
        
        return context

class ContactFormView(BaseFormPage):
    template_name = 'contact.html'
    page_sub_title = 'Contact Us'
    form_class = ContactForm
    success_message = "Message was sent successfully"
#     success_url = '/contact/thanks'
    
    def get(self, request, *args, **kwargs):
    
        return super(ContactFormView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        
        if form.is_valid():

            subject = CONTACT_SUBJECT_EMAILS[int(form.cleaned_data.get('subject'))][0]
            from_email = form.cleaned_data.get('email')
            recipient_list = ['rjbdevel@gmail.com'] #[CONTACT_SUBJECT_EMAILS[int(form.cleaned_data.get('subject'))][1]]
            message = form.cleaned_data.get('message')
            
            try:
                sent_count = send_mail(
                    subject=subject,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    message=message,
                )
#                 raise SMTPAuthenticationError('asdf','asdf')
#                 self.logger.info('sent_count = {}'.format(sent_count))
                if sent_count != 1:

                    messages.error(request, 'Could not send the message. Please try again later.')
                    return render_to_response(
                        self.template_name,
                        context_instance=RequestContext(
                            request,
                            self.get_context_data(form=form)
                        )
                    )
                    
                messages.success(request, self.success_message)
            
            except Exception as e:
                self.logger.info(e.__class__)
                self.logger.info(e)
                messages.error(request, 'Could not send the message. Please try again later.')
            
            return render_to_response(
                self.template_name,
                context_instance=RequestContext(
                    request,
                    self.get_context_data(form=self.form_class)
                )
            )
#             return render(request, self.template_name, {'form': self.form_class})
        
        return self.get(request, args, kwargs)

    def get_context_data(self, **kwargs):
 
        self.init()
        
        context = super().get_context_data(**kwargs)
        return context

#     def form_valid(self, form):
#         self.logger.info('form_valid...')
# 
#  
#         from_email = form.cleaned_data.get('email')
#         message = form.cleaned_data.get('message')
#         send_mail(
#             subject='Subject',
#             message=message,
#             from_email=from_email,
#             recipient_list=['a@b.com'],
#         )
#         return super(ContactFormView, self).form_valid(form)
            
class Help(BaseTemplatePage):
    template_name = 'help.html'
    page_sub_title = 'Help'
    
    def get_context_data(self, **kwargs):
#         self.logger.info(self.page_sub_title)
        
        self.init()
        
        context = super().get_context_data(**kwargs)

        section = context.get('section') or 'topics'
        context['section'] = section
        context['data'] = HELP_DATA[section]
#         self.logger.info('data = {}'.format(context['data']))
        
#         self.logger.info('section = {}'.format(section))
        self.template_name = 'help_{}.html'.format(section)
        
        return context

class Subscriptions(BaseTemplatePage):
    template_name = 'subscriptions.html'
    page_sub_title = 'Subscriptions'

    def get_context_data(self, **kwargs):
#         self.logger.info(self.page_sub_title)
        
        self.init()
        
        context = super().get_context_data(**kwargs)

        subtype = context.get('subtype') or 'artists'
        context['subtype'] = subtype
        if subtype == 'artists':
            context['othersubtype'] = 'organizations'
            context['othersubtypelabel'] = 'Organizations'
        else:
            context['othersubtype'] = 'artists'
            context['othersubtypelabel'] = 'Artists'
        context['headers'] = SUBSCRIPTIONS_DATA['headers'][subtype]
        context['data'] = SUBSCRIPTIONS_DATA[subtype]

        features = [] # To send to the template
        all_features = [ [],[],[] ] # A holding place
        # Get the feature list
        feature_list = SUBSCRIPTIONS_DATA['features']
#         # Create place holders for each level.
#         features = [
#             feature_list.copy(),
#             feature_list.copy(),
#             feature_list.copy(),
#             feature_list.copy()
#         ]
        levels = SUBSCRIPTIONS_DATA[subtype]
        # Get the features for each level. Add each
        # level list to the next level.
        for i in range(len(levels)):
            cur_list = levels[i]['features']
            for j in range(i,len(levels)):
                all_features[j] += cur_list
        
        for i in range(len(feature_list)):
            cur_row = []
            cur_row.append(feature_list[i])
            for j in range(len(all_features)):
                if i in all_features[j]:
                    cur_row.append('check')
                else:
                    cur_row.append('')
            features.append(cur_row)
        context['features'] = features
#         self.logger.info('section = {}'.format(section))
        
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
    
class Error404(BaseTemplatePage):
    template_name = '404.html'
    page_sub_title = 'Page Not Found'

    def get_context_data(self, **kwargs):

        self.init()
        
        context = super().get_context_data(**kwargs)
        
        return context

if __name__ == '__main__':
    image_path = '../static/images/carousel-*'
    carousel_images = glob.glob(image_path)
    print(carousel_images)
    