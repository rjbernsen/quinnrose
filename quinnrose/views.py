# import os
# import glob
import logging
from distutils import util as dis_util
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, FormView

from quinnrose.menu import menu as main_menu
from artist.menu import menu as artist_menu
from artist.temp_data import artist_profiles
from organization.menu import menu as organization_menu
from community.menu import menu as community_menu
from quinnrose.forms import SignInForm, ContactForm, SubscribeForm
from quinnrose.home_page_info import home_page_info
from quinnrose.temp_data import HELP_DATA, SUBSCRIPTIONS, SHARES
from quinnrose.config import CONFIG_CONTEXT, CONTACT_SUBJECT_EMAILS

mock_user = artist_profiles['1']

class BasePage(object):
    default_title = CONFIG_CONTEXT['full_site_name']
    
    logger = logging.getLogger('quinnrose')
    APP = 'quinnrose'

    menus = {
        'quinnrose':    main_menu,
        'artist':       artist_menu,
        'organization': organization_menu,
        'community': community_menu
    }
    
    current_menu = None
    

    print('settings.DEBUG = {}'.format(settings.DEBUG))

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'page_title': self._get_title(),
                'page_header': self.page_sub_title,
                'menu': main_menu,
            }
        )

        context['shares'] = SHARES
        
        context['current_lat'] = self.request.session.get('current_lat', '')
        context['current_lon'] = self.request.session.get('current_lon', '')
        context['current_postal_code'] = self.request.session.get('current_postal_code', '')

        # Must be y, yes, t, true, on, 1 or n, no, f, false, off, 0
        is_bare = dis_util.strtobool(self.request.GET.get('bare', 'false').lower()) == 1
        context['is_bare'] = is_bare
        
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
        self.request.session['current_app'] = self.APP

#         print('home current_lat = {}'.format(self.request.session.get('current_lat')))
        context = super().get_context_data(**kwargs)

#         image_path = ''
#         if settings.IN_PRODUCTION:
#             image_path = os.path.join(settings.STATIC_ROOT, 'images', 'carousel') + '-*'
#         else:
#             image_path = os.path.join(settings.STATIC_MAIN_APP, 'quinnrose', 'images', 'carousel') + '-*'
#             print(settings.STATIC_MAIN_APP)
#             print(image_path)
#         carousel_images = [
#             os.path.basename(p) for p in glob.glob(image_path)
#         ]
#         print(carousel_images)
#         carousel_images.sort()
        
        context.update(
            {
#                 'carousel_images': carousel_images,
                'home_page_info': home_page_info,
#                 'featurettes': featurettes,
            }
        )

        return context

class About(BasePage, TemplateView):
    template_name = 'about.html'
    page_sub_title = 'About Us'

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

        subtype = context.get('subtype') or 'artist'
        context['subtype'] = subtype
        SUBSCRIPTIONS.current_subtype = subtype

        if subtype == 'artist':
            context['othersubtype'] = 'organization'
            context['othersubtypelabel'] = 'Organizations'
        else:
            context['othersubtype'] = 'artist'
            context['othersubtypelabel'] = 'Artists'
        context['headers'] = SUBSCRIPTIONS.headers[subtype]

        data = []
        for s in SUBSCRIPTIONS:
            data.append(s)
        context['data'] = data

        context['features'] = self._get_features(subtype)
        
        return context

    def _get_features(self, subtype):
        features = [] # To send to the template
        all_features = [] # A holding place

        for s in SUBSCRIPTIONS:
            all_features.append([])
        
        # Get the feature list
        feature_list = SUBSCRIPTIONS.features
#         print(feature_list)
        
        # Get the features for each level. Add each
        # level list to the next level.
        i = -1
        SUBSCRIPTIONS.current_subtype = subtype
#         print('Getting features')
        for s in SUBSCRIPTIONS:

            i += 1
            cur_list = s.features
            
            for j in range(i,SUBSCRIPTIONS.count()):
                all_features[j] += cur_list
#         print(all_features)

        # Add check marks for the compare feature list.
        for i in range(len(feature_list)):
            cur_row = {}
            cur_row['feature'] = feature_list[i]
            
            cur_row['checks'] = []
            
            for j in range(len(all_features)):
                if feature_list[i] in all_features[j]:
                    cur_row['checks'].append('check')
                else:
                    cur_row['checks'].append('')
            features.append(cur_row)
#         print(features)
        return features
    
class Subscribe(BasePage, FormView):
    template_name = 'subscribe.html'
    page_sub_title = 'Subscribe'
    form_class = SubscribeForm
    success_message = "Subscribed successfully"
    subtype = None
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        
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
# 
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
 
        context = super().get_context_data(**kwargs)
        
        context['level'] = self.request.GET.get('level', '1')
        context['user'] = mock_user
#         self.subtype = context.get('subtype')
#         print('context self.subtype = {}'.format(self.subtype))

        # Get the data for building the javascript dict.
        # This is for dynamic building of the subscription
        # message as the user clicks on the choices.
        SUBSCRIPTIONS.current_subtype = context.get('subtype')
        js_dict = []

        for s in SUBSCRIPTIONS:
            for key in s.frequency_info:
                cur_row = {}

                freq_info = s.frequency_info[key]
                cur_row['level_id'] = s.sub_id            
                cur_row['freq_id'] = freq_info['freq_id']            
                cur_row['label'] = freq_info['label'].lower()            
                cur_row['price'] = freq_info['price']            
                cur_row['savings'] = freq_info['savings']            
            
                js_dict.append(cur_row)
            
        
        context['js_dict'] = js_dict
#         print(js_dict)
        return context
    
    def get_form_kwargs(self):
#         print('self.kwargs = {}'.format(self.kwargs))
        kwargs = super().get_form_kwargs()
#         print('kwargs self.request.GET[subtype] = {}'.format(self.request.GET.get('subtype', 'shit')))
#         kwargs['subtype'] = self.subtype
        kwargs.update(self.kwargs)
        
        return kwargs

class Help(BasePage, TemplateView):
    template_name = 'help.html'
    page_sub_title = 'Help'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

#         print("context.get('section') = {}".format(context.get('section')))
#         print("context.get('help_app') = {}".format(context.get('help_app')))

        section = context.get('section') or 'topics'
        current_app = self.request.session.get('current_app', self.APP)
        help_app = context.get('help_app') or current_app
#         print('current_app = {}'.format(current_app))
#         print('help_app = {}'.format(help_app))


        context['menu'] = self.menus[current_app]
        context['help_app'] = help_app or self.APP
        context['section'] = section
        
        categories = []
        items = []
        
        for help_category in HELP_DATA:
            categories.append({
                'category': help_category.category,
                'label': help_category.label
            })
            if help_category.category == help_app:
                if section == 'topics':
                    items = help_category.get_topics()
                else:
                    items = help_category.get_faqs()
            
        context['categories'] = categories
        context['items'] = items

        return context

class Privacy(BasePage, TemplateView):
    template_name = 'privacy.html'
    page_sub_title = 'Privacy Policy'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['has_pdf_download'] = True
        
        return context
    
class Terms(BasePage, TemplateView):
    template_name = 'terms.html'
    page_sub_title = 'Terms and Conditions'

    def get(self, request, *args, **kwargs):
    
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['has_pdf_download'] = True

        return context
    
class Error404(BasePage, TemplateView):
    template_name = '404.html'
    page_sub_title = 'Page Not Found'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['last_good_url'] = self.request.session.get('last_good_url')
        
        return context

# if __name__ == '__main__':
#     image_path = '../static/images/carousel-*'
#     carousel_images = glob.glob(image_path)
#     print(carousel_images)
    