
from django.views.generic import TemplateView, FormView

from quinnrose.views import BasePage
from .forms import BlogEntryForm
from .temp_data import blog_entries, blog_entries_dict, categories, latest_comments, tags

class BaseCommunityPage(BasePage):
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'community'
                
        context = super().get_context_data(**kwargs)
        
        context['entries'] = blog_entries
        context['categories'] = categories
        context['tags'] = tags
        context['comments'] = latest_comments
        
        return context

class ListPage(BaseCommunityPage, TemplateView):
    template_name = 'list.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        context['page_type'] = 'list'
        
        return context

class PostPage(BaseCommunityPage, TemplateView):
    template_name = 'post.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        entry_id = context.get('entry_id') or '0'

        context['entry'] = blog_entries_dict[entry_id]
        context['page_type'] = 'post'
        
        return context

class NewPostPage(BaseCommunityPage, FormView):
    template_name = 'new.html'
    page_sub_title = None
    form_class = BlogEntryForm
    success_message = "Blog entry posted successfully"
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        return context
