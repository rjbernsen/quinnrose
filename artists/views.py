
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage

class ArtistsPage(BasePage, TemplateView):
    template_name = 'artists.html'
    page_sub_title = None
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'artists'
                
        context = super().get_context_data(**kwargs)

        return context
