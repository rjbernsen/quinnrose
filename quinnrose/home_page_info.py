class HomePageInfoItem(object):
    """
        Parameters:
        
            label
                The text that will appear on the menu.
            
            url
                The relative path of the page url.
            
            separator
                A flag indicating that there is to be a
                separator rather than a meny item.
            
            Usage:
                
                MenuItem(label)
                    The item will be rendered as text only
                    with no link - e.g. a title.
                
                MenuItem(label, url)
                    The item will be rendered as a standard
                    url link.
                
                MenuItem(separator=True)
                    The item will be rendered as a separator
                    with no title or link.
    """
    
    link_root = '/info'
    
    def __init__(self):
        
        self.title = None
        self.description = None
        self.link = None
        
        self.icon = 'star'
        self.button_text = 'Full story'

    def get_link_path(self):
        return self.link_root + '/' + self.link
    
home_page_info = []

# Number 1
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Key Point #1"
info_item.description = 'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
info_item.link = '1'
home_page_info.append(info_item)

# Number 2
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Key Point #2"
info_item.description = 'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
info_item.link = '2'
home_page_info.append(info_item)

# Number 3
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Key Point #3"
info_item.description = 'Sample content: Artists who participate in performing arts in front of an audience are called performers. Example of this include actors, comedians, dancers, magicians, circus artists, musicians, and singers. Performing arts are also supported by workers in related fields, such as songwriting, choreography and stagecraft. A performer who excels in acting, singing, and dancing is commonly referred to as a "triple threat". Performers often adapt their appearance, such as with costumes and stage makeup, stage lighting, and sound.'
info_item.link = '3'
home_page_info.append(info_item)

if __name__ == "__main__":
    print(home_page_info)
    