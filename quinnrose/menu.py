from quinnrose.tools import Menu, MenuItem

# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

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
    