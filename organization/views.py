
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage
from organization.temp_data import organization_profiles

class OrganizationPage(BasePage, TemplateView):
    template_name = 'organization.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'organization'
                
        context = super().get_context_data(**kwargs)
        
        organization_id = context.get('organization_id') or '1'
#         print(organization_profiles[organization_id])
        context['organization_profile'] = organization_profiles[organization_id]

        return context
