
from django.views.generic import TemplateView, FormView
from django.shortcuts import render_to_response
from django.template import RequestContext

from quinnrose.views import BasePage
from quinnrose.file_upload import handle_uploaded_file
from quinnrose.config import CONFIG_CONTEXT
from .menu import menu
from .forms import BlogEntryForm, CommentsForm
from .temp_data import blog_entries, blog_entries_dict, categories, latest_comments, tags

class BaseCommunityPage(BasePage):
    
    page_sub_title = '{} Community Blog'.format(CONFIG_CONTEXT['company_name'])
    
    def get_context_data(self, **kwargs):
        
        self.request.session['current_app'] = 'community'
                
        context = super().get_context_data(**kwargs)
        
        context['menu'] = menu

        context['entries'] = blog_entries
        context['categories'] = categories
        context['tags'] = tags
        context['comments'] = latest_comments
        
        return context

class ListPage(BaseCommunityPage, TemplateView):
    template_name = 'list.html'
    page_sub_title = '{} Community Blog'.format(CONFIG_CONTEXT['company_name'])
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        context['page_type'] = 'list'
        
        return context

class PostPage(BaseCommunityPage, FormView):
    template_name = 'post.html'
    form_class = CommentsForm
    success_message = "Comment posted successfully"
    
#     star_count = 5
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        entry_id = context.get('entry_id') or '0'

        context['entry'] = blog_entries_dict[entry_id]
        context['page_type'] = 'post'
        
        return context

class NewPostPage(BaseCommunityPage, FormView):
    template_name = 'new.html'
    form_class = BlogEntryForm
    success_message = "Blog entry posted successfully"
    
    def post(self, request, *args, **kwargs):

        print("request.FILES['file'] = {}".format(request.FILES['file'].name))
        print("request.FILES['file'] = {}".format(request.FILES['file'].size))
        
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
#             form.save()
            handle_uploaded_file(request.FILES['file'])
            
            return render_to_response(
                self.template_name,
                context_instance=RequestContext(
                    request,
                    self.get_context_data(form=self.form_class)
                )
            )
        
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        return context
