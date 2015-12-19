from datetime import datetime

CATEGORIES = [
    ['1', 'Cabaret'],
    ['2', 'Concert'],
    ['3', 'Fabulous'],
    ['4', 'Milestone'],
    ['5', 'Theater']
]

class BlogEntry(object):
    title = ''
    leader = ''
    article = ''
    entry_date = datetime.now()
    categories = []
    tags = []
    
    DATE_FORMAT = '%B X%d, %Y X%I:%M %p'
    
    def __init__(self,
        title,
        leader,
        article,
        categories=[],
        tags=[],
        entry_date=datetime.now()
    ):
        self.id = None
        self.title = title
        self.leader = leader
        self.article = article
        self.categories = categories
        self.tags = tags
        self.entry_date = entry_date
        self.comments = []
    
    def add_comment(self, comment):
        self.comments.append(comment)
    
    def comment_count(self):
        return len(self.comments)
    
    def get_comments(self):
        return self.comments
    
    def get_date(self):
        return self.entry_date.strftime(self.DATE_FORMAT).replace('X0','').replace('X','')

class BlogComment(object):
    name = ''
    comment_date = datetime.now()
    comment = ''
    
    DATE_FORMAT = '%Y X%I:%M %p on %B X%d'
    
    def __init__(self,
        name,
        comment,
        comment_date=datetime.now()
    ):
        self.name = name
        self.comment = comment
        self.comment_date = comment_date

    def get_date(self):
        return self.comment_date.strftime(self.DATE_FORMAT).replace('X0','').replace('X','')

blog_entries = []

entry = BlogEntry(
    'Talent Connection registers first 1000 artists',
    'After a very short period in existence, QuinnRose Talent Connection has already reached 1000+ artists registered for the game-changing website.',
    'The artist known as "Fabulous Shannon" was the 1000th person to register with the us. She marks an important achievement for the website and we are thankful that she has the distinction of pushing us over this milestone. She will receive a lifetime full subscription as a gift!',
    ['Milestone', 'Fabulous'],
    ['Company News', 'Artists', 'New Members', 'Free Stuff', 'Milestones']
)
entry.add_comment(
    BlogComment(
        'Eduardo',
        'Yay sweetheart!'
    )
)
entry.add_comment(
    BlogComment(
        'Shannon',
        '<3'
    )
)
entry.add_comment(
    BlogComment(
        'Ferdinand',
        'Jealous!!!'
    )
)
blog_entries.append(entry)

entry = BlogEntry(
    'Welcome PMT Productions',
    'Greetings to the latest addition to the community: PMT Productions - otherwise known as Pitch Me This Productions! Founder and Artistic Director Eduardo Guzman has brought a new and unique facet to the Houston performing arts community.',
    'PMT has been active in the Houston entertainment scene for two years and already has a solid fan base that has come to expect nothing but the very best from this young company. Look for their performance events to be announced very soon, and don\'t miss a single one of them! You\'ll enjoy every minute of their endeavors, be it theater, cabaret, or seasonal concerts.',
    ['Theater', 'Cabaret', 'Concert'],
    ['Company News', 'Organizations', 'New Members']
)
entry.add_comment(
    BlogComment(
        'Joseph',
        'Welcome PMT! Can\'t wait to see one of your productions!'
    )
)
entry.add_comment(
    BlogComment(
        'Mary',
        'Saw Rocky Horror Show last weekend. Never seen anything like it!!'
    )
)
entry.add_comment(
    BlogComment(
        'Jesus',
        'Damn I missed Rocky! Will it be an annual thing?'
    )
)
blog_entries.append(entry)

categories = []
tags = []
latest_comments = []
blog_entries_dict = {}

for i in range(len(blog_entries)):
    blog_entries[i].id = i
    blog_entry = blog_entries[i]
    
    categories.extend(x for x in blog_entry.categories if x not in categories)
    tags.extend(x for x in blog_entry.tags if x not in tags)

    for comment in blog_entry.comments:
        latest_comments.append({'comment':comment.comment, 'name':comment.name, 'entry_id': blog_entry.id})

    blog_entries_dict[str(i)] = blog_entry

# print(blog_entries[1].__dict__)
categories.sort()
tags.sort()

