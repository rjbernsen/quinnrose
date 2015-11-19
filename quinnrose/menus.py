class Menu(object):
    
    def __init__(self, label=None):
        
        self.label = label

        self.left = True
        self.right = False
        self.is_dropdown = False
        
        self.items = []
    
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

main_menus = []

# Main Menu Items
# --------------------------------------
menu = Menu()

item = MenuItem(
    label='Artists',
    url='/artists'
)
menu.addItem(item)

item = MenuItem(
    label='Organizations',
    url='/organizations'
)
menu.addItem(item)

item = MenuItem(
    label='About',
    url='/about'
)
menu.addItem(item)

item = MenuItem(
    label='Contact',
    url='/contact'
)
menu.addItem(item)

main_menus.append(menu)

# Membership Dropdown
# --------------------------------------
menu = Menu()
menu.label = 'Membership'
menu.is_dropdown = True
menu.right = True

item = MenuItem(
    label='Sign in',
    url='/signin'
)
menu.addItem(item)

item = MenuItem(
    label='Register',
    url='/register'
)
menu.addItem(item)

item = MenuItem(
    separator=True
)
menu.addItem(item)

item = MenuItem(
    label='Subscriptions'
)
menu.addItem(item)

item = MenuItem(
    label='Basic',
    url='/subscriptions#basic'
)
menu.addItem(item)

item = MenuItem(
    label='Premium',
    url='/subscriptions#premium'
)
menu.addItem(item)

main_menus.append(menu)

# Help Dropdown
# --------------------------------------
menu = Menu()
menu.label = 'Help'
menu.is_dropdown = True
menu.right = True

item = MenuItem(
    label='Topics',
    url='/help#topics'
)
menu.addItem(item)

item = MenuItem(
    label='FAQs',
    url='/help#faqs'
)
menu.addItem(item)

main_menus.append(menu)
