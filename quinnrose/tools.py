"""
This module contains several classes that are used throughout
all applications.
"""
class Menu(object):
    
    def __init__(self, label=None):
        
        self.label = label

        self.left = True
#         self.right = False
        self.is_dropdown = False
        
        self.items = []
#         self.dropdown_menus = []
    
    def addItem(self, menu_item):
        
        self.items.append(menu_item)
    
    def getItems(self):
        
        return self.items

class MenuItem(object):
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
    def __init__(self, label=None, url=None, separator=False):
        
        self.label = label
        self.url = url
        self.separator = separator
        self.is_dropdown = False

    def getId(self):
        
        return "menu_{}".format(self.label.replace(' ','_').lower())
    
class Featurette(object):
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
    
    def __init__(self):
        
        self.title = None
        self.sub_title = None
        self.description = None
        
        self.image_file_name = None

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
    
