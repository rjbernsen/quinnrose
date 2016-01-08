from urllib.parse import urlparse
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils.datastructures import MultiValueDictKeyError
from quinnrose.geonames import GeonamesClient
from quinnrose.pdf_manager import PDFGenerator

# This is used to set session data from an AJAX request.
def session_handler(request):
    data = request.POST
#     print(data)
    if not request.is_ajax() or (request.POST and not request.method=='POST'):
        return HttpResponseNotAllowed(['POST'])
 
    for key in data.keys():
#         print(data[key])
        request.session[key] = data[key]
#     print()
#     print('current_lat = {}'.format(request.session['current_lat']))
    return HttpResponse('ok')

def geonames_handler(request):
    retval = 'error'
    data = request.GET

    if not request.is_ajax() or (request.GET and not request.method=='GET'):
        return HttpResponseNotAllowed(['GET'])

    if not 'command' in data:
        retval = 'No command found!'
    else:

        req_cmd = data['command']
        
        if req_cmd == 'get_postal_code':
            if not 'current_lat' in data or not 'current_lon' in data:
                retval = 'Lat and lon are required to get the postal code!'
            else:
                gc = GeonamesClient()
                try:
                    retval = gc.get_postal_code(data['current_lat'], data['current_lon'])
                    request.session['current_postal_code'] = retval
                except MultiValueDictKeyError as e:
                    retval = 'Bad key name: {}'.format(str(e).replace('"',''))
                except Exception as e:
                    print(e.__class__)
        
    return HttpResponse(retval)

def pdf_handler(request):
    data = request.GET
#     print('data = {}'.format(data))
#     print('request.is_ajax() = {}'.format(request.is_ajax()))
#     print('request.method = {}'.format(request.method))

    if request.GET and not request.method == 'GET':
        return HttpResponseNotAllowed(['GET'])

    if not 'from_url' in data:
        response = 'URL not found!'
    else:

        from_url = data['from_url']
        
        delim = '?'
        if delim in from_url:
            delim = '&'
        
        from_url += '{}bare=True'.format(delim)
#         print('from_url = {}'.format(from_url))
        
        pg = PDFGenerator()
        
        pdf = pg.get_pdf(from_url)
#         print('pdf[0:10] = {}'.format(pdf[0:10]))
        
        file_name = urlparse(from_url).path[1:]
        if file_name == '/' or not file_name:
            file_name = 'quinnrose'
        file_name = '{}.pdf'.format(file_name.replace('/','_'))
#         print('file_name = {}'.format(file_name))
        
#         response = HttpResponse(pdf, content_type='application/pdf')
        response = HttpResponse(pdf)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        response.set_cookie('fileDownload', 'true', path='/')

    return response
