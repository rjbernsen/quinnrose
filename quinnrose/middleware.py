# Add logic here that should be processed for
# all views.
class MySessionProcessingMiddleware(object):

#     def process_request(self, request):
#         # Add a session value for all requests
#         request.session['last_url'] = request.build_absolute_uri() + ' - 1'

    # your desired cookie will be available in every HttpResponse parser like browser but not in django view
    def process_response(self, request, response):
        
#         print('MySessionProcessingMiddleware.process_response')
#         print('response.status_code = {}'.format(response.status_code))
#         print('response.keys() = {}'.format(response.keys()))
        if hasattr(response, 'template_name'):
            if response.template_name:
                if not '404.html' in response.template_name:
                
                    request.session['last_good_url'] = request.build_absolute_uri()
#         print('request.session.last_good_url = {}'.format(request.session['last_good_url']))
#         print('response = {}'.format(response.template_name))

        return response


class PDFRenderingMiddleware(object):

    def process_response(self, request, response):
        if hasattr(response, 'context_data'):
            if 'is_bare' in response.context_data:
                is_bare = response.context_data['is_bare']
                
                if is_bare:
                    content = response.content

                    replaced_content = content.replace(bytes('col-md', 'utf-8'), bytes('col-xs', 'utf-8'))
                    replaced_content = replaced_content.replace(bytes('page-header-byline', 'utf-8'), bytes('page-header-byline-pdf', 'utf-8'))

                    response.content = replaced_content

        return response
