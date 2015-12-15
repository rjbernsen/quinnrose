import os
import glob
import logging
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import TemplateView, FormView
# from django.contrib.messages.views import SuccessMessageMixin

from quinnrose.menu import menu as main_menu
from artist.menu import menu as artist_menu
from organization.menu import menu as organization_menu
from quinnrose.forms import SignInForm, ContactForm
from quinnrose.home_page_info import home_page_info
from quinnrose.featurettes import featurettes
from quinnrose.temp_data import HELP_DATA, SUBSCRIPTIONS_DATA
from quinnrose.config import CONFIG_CONTEXT, CONTACT_SUBJECT_EMAILS

class BasePage(object):
    default_title = CONFIG_CONTEXT['full_site_name']
    page_sub_title = None
    
    logger = logging.getLogger('quinnrose')

    menus = {
        'quinnrose':    main_menu,
        'artist':       artist_menu,
        'organization': organization_menu
    }
    
    current_menu = None
    
    def get_context_data(self, **kwargs):

        current_app = self.request.session.get('current_app', 'quinnrose')
#         print('current_app = {}'.format(current_app))

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'page_title': self._get_title(),
                'page_header': self.page_sub_title,
                'menu': self.menus[current_app],
            }
        )
        context.update(self.kwargs)
        context.update(CONFIG_CONTEXT)
        
        return context

    def _get_title(self):
        
        if self.page_sub_title:
            page_title = '{} - {}'.format(self.default_title,self.page_sub_title)
        else:
            page_title = self.default_title
        
        return page_title
    
class HomePage(BasePage, TemplateView):
    template_name = 'home.html'
    page_sub_title = None
    
    def get_context_data(self, **kwargs):
        self.request.session['current_app'] = 'quinnrose'

        context = super().get_context_data(**kwargs)

        image_path = ''
        if settings.IN_PRODUCTION:
            image_path = os.path.join(settings.STATIC_ROOT, 'images', 'carousel') + '-*'
        else:
            image_path = os.path.join(settings.STATIC_MAIN_APP, 'images', 'carousel') + '-*'
        carousel_images = [
            os.path.basename(p) for p in glob.glob(image_path)
        ]
        carousel_images.sort()
        
        context.update(
            {
                'carousel_images': carousel_images,
                'home_page_info': home_page_info,
                'featurettes': featurettes,
            }
        )

        return context

class About(BasePage, TemplateView):
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
        
        context = super().get_context_data(**kwargs)

        section = context.get('section') or '1'
        
        self.template_name = 'about_{}.html'.format(self.sections[int(section)])
        
        return context

class ContactFormView(BasePage, FormView):
    template_name = 'contact.html'
    page_sub_title = 'Contact Us'
    form_class = ContactForm
    success_message = "Message was sent successfully"
    
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
        
        return self.get(request, args, kwargs)

    def get_context_data(self, **kwargs):
 
        context = super().get_context_data(**kwargs)
        return context

class SignInFormView(BasePage, FormView):
    template_name = 'signin_{}.html'
    page_sub_title = 'Sign In'
    form_class = SignInForm
    
    sub_titles = {
        'signin': 'Sign in',
        'register': 'Register'
    }

    def get_context_data(self, **kwargs):
        subtype = self.kwargs.get('subtype') or 'signin'
 
        self.page_sub_title = self.sub_titles[subtype]
        
        context = super().get_context_data(**kwargs)
        context['subtype'] = subtype

        self.template_name = self.template_name.format(subtype)
        
        return context

class Subscriptions(BasePage, TemplateView):
    template_name = 'subscriptions.html'
    page_sub_title = 'Subscriptions'

    def get_context_data(self, **kwargs):
        
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

        context['features'] = self._get_features(subtype)
        
        return context

    def _get_features(self, subtype):
        features = [] # To send to the template
        all_features = [ [],[],[] ] # A holding place
        # Get the feature list
        feature_list = SUBSCRIPTIONS_DATA['features']
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

        return features
    
class Help(BasePage, TemplateView):
    template_name = 'help.html'
    page_sub_title = 'Help'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        section = context.get('section') or 'topics'

        context['section'] = section
        context['data'] = HELP_DATA[section]

        return context

class Privacy(BasePage, TemplateView):
    template_name = 'privacy.html'
    page_sub_title = 'Privacy Policy'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context
    
class Terms(BasePage, TemplateView):
    template_name = 'terms.html'
    page_sub_title = 'Terms and Conditions'

    def get(self, request, *args, **kwargs):
    
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context
    
class Error404(BasePage, TemplateView):
    template_name = '404.html'
    page_sub_title = 'Page Not Found'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['last_good_url'] = self.request.session.get('last_good_url')
        
        return context

if __name__ == '__main__':
    image_path = '../static/images/carousel-*'
    carousel_images = glob.glob(image_path)
    print(carousel_images)
    