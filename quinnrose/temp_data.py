"""
Temporary data to be used until the database
models have been created.
"""

from quinnrose.utils import isfloat

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

# DO NOT CHANGE THESE VALUES!!!!!!
SUBSCRIPTION_BILLING_FREQUENCY = [
    [1, 'Monthly'],
    [2, 'Yearly']
]

class SubscriptionHeader(object):
    
    def __init__(self, header, description):
        self.header = header
        self.description = description

class SubscriptionFeature(object):
    
    def __init__(self, feat_id, feature):
        self.feat_id = feat_id
        self.feature = feature

class SubscriptionBillingFrequency(object):
    
    def __init__(self, freq_id, billing_frequency):
        self.freq_id = freq_id
        self.billing_frequency = billing_frequency
        
class SubscriptionBillingFrequencies(object):
    
    frequencies = []
    
    def __init__(self):
        for freq in SUBSCRIPTION_BILLING_FREQUENCY:
            sbf = SubscriptionBillingFrequency(
                freq[0],
                freq[1]
            )
            self.frequencies.append(sbf)

    def __iter__(self):
        self.cur_sub_idx = -1
        return self
    
    def __next__(self):
        self.cur_sub_idx += 1
        
        try:
            return self.frequencies[self.cur_sub_idx]
        except:
            
            raise StopIteration
    
    def count(self):
        return len(self.frequencies)
    
class Subscriptions(object):

    subtypes = ['artist', 'organization']
    
    frequencies = SubscriptionBillingFrequencies()

    headers = {}
    features = []
    subscriptions = {}
    
    current_subtype = None # For the iterator!
    
    def __init__(self):
        for key in SUBSCRIPTIONS_HEADERS:
            self._add_header(
                key,
                SUBSCRIPTIONS_HEADERS[key]['header'],
                SUBSCRIPTIONS_HEADERS[key]['description']
            )

        self.features = SUBSCRIPTION_FEATURES

        for subtype in self.subtypes:
            self.subscriptions[subtype] = []
            
    def __iter__(self):
        self.cur_sub_idx = -1
        return self
    
    def __next__(self):
        self.cur_sub_idx += 1
        
        try:
            s = self.subscriptions[self.current_subtype][self.cur_sub_idx]
            
            if not s.already_generated:
                s.frequency_info = {}
                
                for freq in self.frequencies:
                    s.frequency_info[freq.billing_frequency.lower()] = {}
                    symbol = '$'
                    if s.prices[freq.freq_id - 1] == 'Free':
                        symbol = ''
                    s.frequency_info[freq.billing_frequency.lower()]['freq_id'] = freq.freq_id
                    s.frequency_info[freq.billing_frequency.lower()]['label'] = freq.billing_frequency
                    s.frequency_info[freq.billing_frequency.lower()]['price'] = symbol + s.prices[freq.freq_id - 1]
                    symbol = ''
#                     print(s.yearly_savings)

                    if s.yearly_savings:
                        symbol = '$'
                        s.frequency_info[freq.billing_frequency.lower()]['savings'] = symbol + s.yearly_savings
                    else:
                        s.frequency_info[freq.billing_frequency.lower()]['savings'] = None
                    
                for i in range(len(s.features)):
                    s.features[i] = self.features[s.features[i]]
                s.already_generated = True

            return s
        except:
            
            raise StopIteration
    
    def count(self, subtype=None):
        if not subtype:
            subtype = self.current_subtype
        
        return len(self.subscriptions[subtype])
    
    def get_choices(self, subtype=None):
        retval = []

        if not subtype:
            subtype = self.current_subtype

        for s in self.subscriptions[subtype]:
            retval.append([s.sub_id, s.level])

        return retval
    
    def add_subscription(self, subscription):
        self.subscriptions[subscription.subtype].append(subscription)

    def _add_header(self, subtype, header, description):
        sh = SubscriptionHeader(header, description)
        self.headers[subtype] = sh

class Subscription(object):

    def __init__(self,
        subtype,
        sub_id,
        level,
        description,
        prices,
        benefits,
        features
    ):
    
        self.subtype = subtype
        self.sub_id = sub_id
        self.level = level
        self.description = description
        self.prices = prices
        self.details = benefits
        self.features = features
        if isfloat(prices[0]):
            self.yearly_savings = str(round((float(prices[0]) * 12) - float(prices[1]),2))
        else:
            self.yearly_savings = None
        
        self.already_generated = False

    def get_image_name(self):
        return "{}_{}.jpg".format(self.subtype, self.sub_id)

SUBSCRIPTIONS = Subscriptions()

s = Subscription(
    'artist',
    1,
    'Viewer',
    'View artist and organization profiles - unlimited!',
    ['Free', 'Free'],
    [
        'View basic artist information',
        'View basic organization information',
        'Create basic artist profile',
        'Search other artists by zip code',
        'Search organizations by zip code'
    ],
    [0,1,2,3,4,5]
)
SUBSCRIPTIONS.add_subscription(s)

s = Subscription(
    'artist',
    '2',
    'Seeker',
    'Contact other artists and organizations - unlimited!',
    ['1.99', '21.99'],
    [
        'All "Viewer" features, plus...',
        'Search for other artists using advanced criteria',
        'Search for organizations using advance criteria',
        'Contact other artists or organizations via the web site',
        'Search auditions'
    ],
    [6,7,8,9,10,11]
)
SUBSCRIPTIONS.add_subscription(s)

s = Subscription(
    'artist',
    3,
    'Doer',
    'Appear in search results by organizations seeking artists - unlimited!',
    ['3.99',  '43.99'],
    [
        'All "Seeker" features, plus...',
        'Show up in organization searches',
        'Build your online resume/portfolio'
    ],
    [12,13,14,15]
)
SUBSCRIPTIONS.add_subscription(s)

s = Subscription(
    'organization',
    1,
    'Writer',
    'View artist and organization profiles - unlimited!',
    ['Free',  'Free'],
    [
        'View basic artist information',
        'View basic organization information',
        'Create basic profile for your organization',
        'Search artists by zip code',
        'Search organizations by zip code'
    ],
    [0,1,2,3,4,5]
)
SUBSCRIPTIONS.add_subscription(s)

s = Subscription(
    'organization',
    2,
    'Director',
    'Contact other artists and organizations - unlimited!',
    ['7.99', '91.99'],
    [
        'All "Writer" features, plus...',
        'Search for artists using advanced criteria',
        'Search for organizations using advance criteria',
        'Contact artists or organizations via the web site',
        'Register events',
        'Announce auditions'
    ],
    [6,7,8,9,10,11]
)
SUBSCRIPTIONS.add_subscription(s)

s = Subscription(
    'organization',
    3,
    'Producer',
    'Appear in search results by organizations seeking artists - unlimited!',
    ['11.99', '129.99'],
    [
        'All "Director" features, plus...',
        'Upload event photos',
        'Interface profiles and events with social media'
    ],
    [12,13,14,15]
)
SUBSCRIPTIONS.add_subscription(s)

CREDIT_CARD_TYPES = [
    ('visa', 'Visa'),
    ('mastercard', 'MasterCard'),
    ('amex', 'American Express'),
    ('discover', 'Discover'),
    ('diners', 'Diners'),
    ('paypal', 'PayPal'),
    ('google', 'Google Checkout'),
    ('amazon', 'Amazon Pay')
]
if __name__ == "__main__":
    
    SUBSCRIPTIONS.current_subtype = 'artist'
    
    for s in SUBSCRIPTIONS:
        print('{} {}'.format(s.subtype, s.level))
