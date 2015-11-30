class Menu(object):
    
    def __init__(self, label=None):
        
        self.label = label

        self.left = True
        self.right = False
        self.is_dropdown = False
        
        self.items = []
        self.dropdown_menus = []
    
    def addItem(self, menu_item):
        
        self.items.append(menu_item)
    
    def addDropdownMenu(self, dropdown_menu):
        
        self.dropdown_menus.append(dropdown_menu)
        
    def getItems(self):
        
        return self.items

    def getDropdownMenus(self):
        
        return self.dropdown_menus

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

    def getId(self):
        
        return "menu_{}".format(self.label.replace(' ','_').lower())
    
# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

# item = MenuItem(
#     label='Artists',
#     url='/artists'
# )
# menu.addItem(item)
# 
# item = MenuItem(
#     label='Organizations',
#     url='/organizations'
# )
# menu.addItem(item)

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

# Membership Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Membership'
dropdown_menu.is_dropdown = True
dropdown_menu.right = True

item = MenuItem(
    label='Sign in',
    url='/signin'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Register',
    url='/signin/register'
)
dropdown_menu.addItem(item)

item = MenuItem(
    separator=True
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Subscriptions'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Artists',
    url='/subscriptions/artists'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Organizations',
    url='/subscriptions/organizations'
)
dropdown_menu.addItem(item)

menu.addDropdownMenu(dropdown_menu)

# Help Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Help'
dropdown_menu.is_dropdown = True
dropdown_menu.right = True

item = MenuItem(
    label='Topics',
    url='/help/topics'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='FAQs',
    url='/help/faqs'
)
dropdown_menu.addItem(item)

menu.addDropdownMenu(dropdown_menu)

if __name__ == "__main__":
    print(menu)
    