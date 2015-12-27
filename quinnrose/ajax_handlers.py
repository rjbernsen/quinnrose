from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils.datastructures import MultiValueDictKeyError
from quinnrose.geonames import GeonamesClient

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
