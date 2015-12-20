import os
from django.conf import settings

def handle_uploaded_file(file_object):
    
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
        
    full_file_path = os.path.join(settings.MEDIA_ROOT, file_object.name)
    
    with open(full_file_path, 'wb+') as destination:
        for chunk in file_object.chunks():
            destination.write(chunk)