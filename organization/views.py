import os
import glob

from django.conf import settings
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage
from .menu import menu
from .temp_data import organization_profiles

class BaseOrganizationPage(BasePage):
    template_name = 'organization.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'organization'
                
        context = super().get_context_data(**kwargs)

        context['menu'] = menu

        organization_id = context.get('organization_id') or 'pmt'
#         print(organization_profiles[organization_id])
        try:
            context['organization_profile'] = organization_profiles[organization_id]
        except KeyError:
            context['what'] = 'organization'
            context['last_good_url'] = self.request.session.get('last_good_url')
            self.template_name = 'record_not_found.html'
            return context
        
        self.organization_id = organization_id
        
        context['org_id'] = organization_id

        return context
    
class OrganizationPage(BaseOrganizationPage, TemplateView):
    template_name = 'organization.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
#         print(os.path.dirname(os.path.realpath(__file__)))
        app_path = os.path.dirname(os.path.realpath(__file__))
#         print('app_path = {}'.format(app_path))

        image_path = ''
        if settings.IN_PRODUCTION:
            image_path = os.path.join(settings.STATIC_ROOT, 'organization', 'images', 'organizations', self.organization_id, 'carousel', 'main') + '_*'
        else:
            image_path = os.path.join(app_path, 'static', 'organization', 'images', 'organizations', self.organization_id, 'carousel', 'main') + '_*'
#         print('image_path = {}'.format(image_path))

        carousel_images = [
            os.path.basename(p) for p in glob.glob(image_path)
        ]
        carousel_images.sort()
        
        for i in range(len(carousel_images)):
            carousel_images[i] = {
                'image' : carousel_images[i],
                'thumb' : carousel_images[i].replace('main', 'thumb')
            }
        
        context['carousel_images'] = carousel_images
        
        return context
