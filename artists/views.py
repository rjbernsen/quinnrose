import logging

from django.conf import settings
from django.views.generic import TemplateView, FormView

from quinnrose.config import CONFIG_CONTEXT

class BasePage(object):
    default_title = CONFIG_CONTEXT['full_site_name']
    
    logger = logging.getLogger('quinnrose')

    def init(self, extra_page_context={}):
        self.context = {
            'page_title': self._get_title(),
            'page_header': self.page_sub_title,
#             'menu': menu,
        }
        
        self.context.update(extra_page_context)
        self.context.update(CONFIG_CONTEXT)
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.update(self.context)
        context.update(self.kwargs)
        
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

class ArtistsPage(BaseTemplatePage):
    template_name = 'artists.html'
    page_sub_title = None
    
    def get_context_data(self, **kwargs):
        

        more_page_context = {
#             'carousel_images': carousel_images,
#             'home_page_info': home_page_info,
#             'featurettes': featurettes,
        }

        self.init(more_page_context)
    
        context = super().get_context_data(**kwargs)
        

        return context
