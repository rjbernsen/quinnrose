"""
Temporary data to be used until the database
models have been created.
"""

HELP_DATA = []

class Help(object):
    
    def __init__(self, category, label):
        self.category = category
        self.label = label

        self.topics = []
        self.faqs = []
    
    def add_topic(self, item):
        self.topics.append(item)
    
    def add_faq(self, item):
        self.faqs.append(item)

    def get_topics(self):
        return self.topics
    
    def get_faqs(self):
        return self.faqs
    
class HelpItem(object):
    
    def __init__(self,
        
        header,
        content
    ):
        self.header = header
        self.content = content

h = Help('quinnrose', 'General')
h.add_topic(
    HelpItem(
        'General Topic 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'General Topic 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'General Topic 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'General Topic 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'General Topic 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'General FAQ 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'General FAQ 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'General FAQ 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'General FAQ 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'General FAQ 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
HELP_DATA.append(h)

h = Help('artist', 'Artists')
h.add_topic(
    HelpItem(
        'Artists Topic 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Artists Topic 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Artists Topic 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Artists Topic 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Artists Topic 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Artists FAQ 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Artists FAQ 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Artists FAQ 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Artists FAQ 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Artists FAQ 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
HELP_DATA.append(h)

h = Help('organization', 'Organizations')
h.add_topic(
    HelpItem(
        'Organization Topic 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Organization Topic 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Organization Topic 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Organization Topic 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Organization Topic 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Organization FAQ 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Organization FAQ 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Organization FAQ 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Organization FAQ 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Organization FAQ 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
HELP_DATA.append(h)

h = Help('community', 'Community')
h.add_topic(
    HelpItem(
        'Community Topic 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Community Topic 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Community Topic 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Community Topic 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_topic(
    HelpItem(
        'Community Topic 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Community FAQ 1',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Community FAQ 2',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Community FAQ 3',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Community FAQ 4',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
h.add_faq(
    HelpItem(
        'Community FAQ 5',
        'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
    )
)
HELP_DATA.append(h)


SUBSCRIPTIONS_HEADERS = {
    'artist': {
        'header': 'For our artists...',
        'description': '...we have three different subscription packages, all designed to provide the talented individual with exactly the right tools for sharing his/her skills.'
    },
    'organization': {
        'header': 'For our organizations...',
        'description': '...we have three different subscription packages, all designed to provide any organization with tools connect with artists and share their events.'
    }
}
SUBSCRIPTIONS_ARTIST = [
    {
        'level': 'Viewer',
        'image': '1.jpg',
        'description': 'View artist and organization profiles - unlimited!',
        'price_per_month': 'Free',
        'price_per_year': 'Free',
        'details': [
            'View basic artist information',
            'View basic organization information',
            'Create basic artist profile',
            'Search other artists by zip code',
            'Search organizations by zip code'
        ],
        'features': [0,1,2,3,4,5]
    },
    {
        'level': 'Seeker',
        'image': '2.jpg',
        'description': 'Contact other artists and organizations - unlimited!',
        'price_per_month': '$1.99',
        'price_per_year': '$21.99',
        'details': [
            'All "Viewer" features, plus...',
            'Search for other artists using advanced criteria',
            'Search for organizations using advance criteria',
            'Contact other artists or organizations via the web site',
            'Search auditions'
        ],
        'features': [6,7,8,9,10,11]
    },
    {
        'level': 'Doer',
        'image': '3.jpg',
        'description': 'Appear in search results by organizations seeking artists - unlimited!',
        'price_per_month': '$3.99',
        'price_per_year': '$43.99',
        'details': [
            'All "Seeker" features, plus...',
            'Show up in organization searches',
            'Build your online resume/portfolio'
        ],
        'features': [12,13,14,15]
    },
]
SUBSCRIPTIONS_ORGANIZATION = [
    {
        'level': 'Writer',
        'image': 'writer.jpg',
        'description': 'View artist and organization profiles - unlimited!',
        'price_per_month': 'Free',
        'price_per_year': 'Free',
        'details': [
            'View basic artist information',
            'View basic organization information',
            'Create basic profile for your organization',
            'Search artists by zip code',
            'Search organizations by zip code'
        ],
        'features': [0,1,2,3,4,5]
    },
    {
        'level': 'Director',
        'image': 'director.jpg',
        'description': 'Contact other artists and organizations - unlimited!',
        'price_per_month': '$7.99',
        'price_per_year': '$91.99',
        'details': [
            'All "Writer" features, plus...',
            'Search for artists using advanced criteria',
            'Search for organizations using advance criteria',
            'Contact artists or organizations via the web site',
            'Register events',
            'Announce auditions'
        ],
        'features': [6,7,8,9,10,11]
    },
    {
        'level': 'Producer',
        'image': 'producer.jpg',
        'description': 'Appear in search results by organizations seeking artists - unlimited!',
        'price_per_month': '$11.99',
        'price_per_year': '$129.99',
        'details': [
            'All "Director" features, plus...',
            'Upload event photos',
            'Interface profiles and events with social media'
        ],
        'features': [12,13,14,15]
    },
]
SUBSCRIPTION_FEATURES = [
    'Create profile',               #  0
    'Upload profile photo',         #  1
    'View artists',                 #  2
    'Artist zip code search',       #  3
    'View organizations',           #  4
    'Organization zip code search', #  5
    'View artist details',          #  6
    'Artist criteria search',       #  7
    'Contact artists',              #  8
    'View organization details',    #  9
    'Organization criteria search', # 10
    'Contact organization',         # 11
    'Register events',              # 12
    'Announce auditions',           # 13
    'Upload event photos',          # 14
    'Social media interface'        # 15
]
SUBSCRIPTIONS_DATA = {
    'headers': SUBSCRIPTIONS_HEADERS,
    'artist': SUBSCRIPTIONS_ARTIST,
    'organization': SUBSCRIPTIONS_ORGANIZATION,
    'features': SUBSCRIPTION_FEATURES
}
