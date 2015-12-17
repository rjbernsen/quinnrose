
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage

class CommunityPage(BasePage, TemplateView):
    template_name = 'community.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'community'
                
        context = super().get_context_data(**kwargs)
        
        return context
