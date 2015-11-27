"""
Temporary data to be used until the database
models have been created.
"""

HELP_TOPICS = [
    [
        'Topic 1',
        'Content 1'
    ],
    [
        'Topic 2',
        'Content 2'
    ],
    [
        'Topic 3',
        'Content 3'
    ],
    [
        'Topic 4',
        'Content 4'
    ],
    [
        'Topic 5',
        'Content 5'
    ]
]
HELP_FAQS = [
    [
        'FAQ 1',
        'Content 1'
    ],
    [
        'FAQ 2',
        'Content 2'
    ],
    [
        'FAQ 3',
        'Content 3'
    ],
    [
        'FAQ 4',
        'Content 4'
    ],
    [
        'FAQ 5',
        'Content 5'
    ]
]
HELP_DATA = {
    'topics': HELP_TOPICS,
    'faqs': HELP_FAQS
}

SUBSCRIPTIONS_HEADERS = {
    'artists': {
        'header': 'For our artists...',
        'description': '...we have three different subscription packages, all designed to provide the talented individual with exactly the right tools for sharing his/her skills.'
    },
    'organizations': {
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
        'includes': [
        ]
    },
    {
        'level': 'Seeker',
        'image': '2.jpg',
        'description': 'Contact other artists and organizations - unlimited!',
        'price_per_month': '$1.99',
        'price_per_year': '$21.99',
        'includes': [
        ]
    },
    {
        'level': 'Doer',
        'image': '3.jpg',
        'description': 'Appear in search results by organizations seeking artists - unlimited!',
        'price_per_month': '$3.99',
        'price_per_year': '$43.99',
        'includes': [
        ]
    },
]
SUBSCRIPTIONS_ORGANIZATIONS = [
    {
        'level': 'Writer',
        'image': 'writer.jpg',
        'description': 'View artist and organization profiles - unlimited!',
        'price_per_month': 'Free',
        'price_per_year': 'Free',
        'includes': [
        ]
    },
    {
        'level': 'Director',
        'image': 'director.jpg',
        'description': 'Contact other artists and organizations - unlimited!',
        'price_per_month': '$7.99',
        'price_per_year': '$91.99',
        'includes': [
        ]
    },
    {
        'level': 'Producer',
        'image': 'producer.jpg',
        'description': 'Appear in search results by organizations seeking artists - unlimited!',
        'price_per_month': '$11.99',
        'price_per_year': '$129.99',
        'includes': [
        ]
    },
]
SUBSCRIPTIONS_DATA = {
    'headers': SUBSCRIPTIONS_HEADERS,
    'artists': SUBSCRIPTIONS_ARTIST,
    'organizations': SUBSCRIPTIONS_ORGANIZATIONS
}