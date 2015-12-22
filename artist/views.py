import os
import glob

from django.conf import settings
from django.views.generic import TemplateView #, FormView

from quinnrose.views import BasePage
from .menu import menu
from .temp_data import artist_profiles

class BaseArtistPage(BasePage):
    template_name = 'artist.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'artist'
                
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        
        self.artist_id = context.get('artist_id') or '1'

        try:
            context['artist_profile'] = artist_profiles[self.artist_id]
        except KeyError:
            context['what'] = 'artist'
            context['last_good_url'] = self.request.session.get('last_good_url')
            self.template_name = 'record_not_found.html'

        context['user_id'] = self.artist_id
        
        return context
    
class ArtistPage(BaseArtistPage, TemplateView):
    template_name = 'artist.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        app_path = os.path.dirname(os.path.realpath(__file__))

        image_path = ''
        if settings.IN_PRODUCTION:
            image_path = os.path.join(settings.STATIC_ROOT, 'artist', 'images', 'artists', self.artist_id, 'carousel', 'main') + '_*'
        else:
            image_path = os.path.join(app_path, 'static', 'artist', 'images', 'artists', self.artist_id, 'carousel', 'main') + '_*'

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
