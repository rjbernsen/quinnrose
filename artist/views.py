
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage
from artist.temp_data import artist_profiles

class ArtistPage(BasePage, TemplateView):
    template_name = 'artist.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'artist'
                
        context = super().get_context_data(**kwargs)
        
        artist_id = context.get('artist_id') or '1'
        print(artist_id)
        context['artist_profile'] = artist_profiles[artist_id]

        return context
