
from django.views.generic import TemplateView, FormView

from quinnrose.views import BasePage
from .forms import BlogEntryForm
from .temp_data import blog_entries, blog_entries_dict, categories, latest_comments, tags

class ListPage(BasePage, TemplateView):
    template_name = 'list.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'community'
                
        context = super().get_context_data(**kwargs)
        
        context['entries'] = blog_entries
        context['categories'] = categories
        context['tags'] = tags
        context['comments'] = latest_comments
        
        return context

class PostPage(BasePage, TemplateView):
    template_name = 'post.html'
    page_sub_title = None
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        entry_id = context.get('entry_id') or '0'

        context['entry'] = blog_entries_dict[entry_id]
        context['entries'] = blog_entries
        context['categories'] = categories
        context['tags'] = tags
        context['comments'] = latest_comments
        
        return context

class NewPostPage(BasePage, FormView):
    template_name = 'new.html'
    page_sub_title = None
    form_class = BlogEntryForm
    success_message = "Blog entry posted successfully"
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context['entries'] = blog_entries
        context['categories'] = categories
        context['tags'] = tags
        context['comments'] = latest_comments
        
        return context
