
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage
from artist.temp_data import artist_profile

class ArtistPage(BasePage, TemplateView):
    template_name = 'artist.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'artist'
                
        context = super().get_context_data(**kwargs)
        
        context['artist_profile'] = artist_profile

        return context
