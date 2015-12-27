import urllib.request
import urllib.parse
import urllib.error
import json

from quinnrose.utils import km_to_miles, miles_to_km

BASE_URL = 'http://api.geonames.org/'
USER_NAME = 'quinnrose'
DEFAULT_RADIUS = 10 # Max is 15 on free plan
DEFAULT_COUNTRY = 'US'
MAX_ROWS = 100

class GeonamesError(Exception):
    
    def __init__(self, status):
        Exception.__init__(self, status)        # Exception is an old-school class
        self.status = status
    
    def __str__(self):
        return self.status
    
    def __unicode__(self):
        return str(self.__str__())


class GeonamesClient(object):

    def __init__(self, username=USER_NAME):
        self.username = username

    def get_postal_code(self, lat, lon, with_city=False):
        
        radius = 0
        
        return self.get_postal_codes_in_radius(lat, lon, radius, with_city)[0]
    
    def get_postal_codes_in_radius(self, lat, lon=None, radius=DEFAULT_RADIUS, with_city=False):
        service_name = 'findNearbyPostalCodesJSON'
        
        if not lon:
            # The search is using a postal code, which is
            # in the "lat" parameter and the "lon" is empty.
            params = {'postalcode':lat,'country':DEFAULT_COUNTRY, 'radius': radius}
        else:
            params = {'lat':lat,'lng':lon, 'radius': radius}
        
        results = self._call(service_name, params)
        
        return self._get_postal_codes(results, with_city)
    
    def get_timezone(self, lat, lon):
        service_name = 'timezoneJSON'
        params = {'lat':lat,'lng':lon}

        results = self._call(service_name, params)

        return self._get_timezone(results)
#     def _prepare_params(self, **kwargs):
#         params = kwargs
#         
#         return params
    
    def _call(self, service_name, params=None):
        url = self._build_url(service_name, params)

        try:
            response = urllib.request.urlopen(urllib.request.Request(url))
            json_response = json.loads(response.read().decode('utf8'))
        except urllib.error.URLError:
            raise GeonamesError('API didnt return 200 response.')
        except ValueError:
            raise GeonamesError('API did not return valid json response.')
        except Exception:
            raise GeonamesError('Some strange exception.')
        else:
            msg = 'Geonames Error:'
            if 'status' in json_response:
                msg += ' Code: ' + str(json_response['status']['value'])
                msg += ' - ' + json_response['status']['message']
                raise GeonamesError(msg)
        return json_response

    def _build_url(self, service_name, params=None):
        url = '%s%s?username=%s' % (BASE_URL, service_name, self.username)
        if params:
            if isinstance(params, dict):
                params = dict((k, v) for k, v in list(params.items()) if v is not None)
                
                if 'radius' in params:
                    params['radius'] = miles_to_km(params['radius'])

                params['maxRows'] = MAX_ROWS

                params = urllib.parse.urlencode(params)
            
            url = '%s&%s' % (url, params)
        return url
    
    def _get_postal_codes(self, json_response, with_city):
        retval = []
        
        main_list = json_response['postalCodes']
        
        for d in main_list:
            if with_city:
                retval.append([d['postalCode'], d['placeName']])
            else:
                retval.append(d['postalCode'])
        
        return retval
    
    def _get_timezone(self, json_response):
        
        return json_response['timezoneId']
    
if __name__ == '__main__':

    gc = GeonamesClient()
    
    results = gc.get_postal_codes_in_radius(29.5824916, -95.2162283)
    print(results)
     
    results = gc.get_postal_codes_in_radius(29.5824916, -95.2162283, with_city=True)
    print(results)
       
    results = gc.get_postal_codes_in_radius('77089', with_city=True)
    print('{} results'.format(len(results)))
    print(results)
      
    results = gc.get_timezone(29.5824916, -95.2162283)
    print(results)

    results = gc.get_postal_code(29.5824916, -95.2162283)
    print(results)
