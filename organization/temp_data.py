organization_profiles = {}

organization_profiles['pmt'] = {
    'name': 'PMT Productions, Inc.',
    'admin_id': '1',
}
organization_profiles['up'] = {
    'name': 'United Players, Inc.',
    'admin_id': '1',
}

class SocialLinks(object):
    
    def __init__(self):

        self.items = []
    
    def add_item(self, si):
        
        self.items.append(si)
        
    def get_items(self):

        return self.items
    
class SocialLink(object):
    
    def __init__(self,
        
        label,
        url,
        image
    ):
        self.label = label
        self.url = url
        self.image = image

SOCIAL_LINKS = SocialLinks()

SOCIAL_LINKS.add_item(
    SocialLink(
        'Facebook',
        'http://www.facebook.com',
        'facebook.jpg'
    )
)
SOCIAL_LINKS.add_item(
    SocialLink(
        'Twitter',
        'http://twitter.com',
        'twitter.jpg'
    )
)
SOCIAL_LINKS.add_item(
    SocialLink(
        'Google+',
        'http://plus.google.com',
        'google_plus.jpg'
    )
)
SOCIAL_LINKS.add_item(
    SocialLink(
        'YouTube',
        'http://www.youtube.com',
        'youtube.jpg'
    )
)

