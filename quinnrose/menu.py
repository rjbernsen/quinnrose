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

# Sign in Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Sign in'
dropdown_menu.is_dropdown = True
# dropdown_menu.right = True

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

menu.addItem(dropdown_menu)

# Subscription Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Subscription'
dropdown_menu.is_dropdown = True
# dropdown_menu.right = True

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

item = MenuItem(
    label='Samples (Temporary)'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Shannon',
    url='/artist/1'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='PMT',
    url='/organization/1'
)
dropdown_menu.addItem(item)

menu.addItem(dropdown_menu)

# Help Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Help'
dropdown_menu.is_dropdown = True
# dropdown_menu.right = True

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

menu.addItem(dropdown_menu)

if __name__ == "__main__":
    print(menu)
    