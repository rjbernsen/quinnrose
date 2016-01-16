from quinnrose.tools import Menu, MenuItem

# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

# Temporary Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Temporary'
dropdown_menu.is_dropdown = True
# dropdown_menu.right = True

item = MenuItem(
    label='Samples'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Shannon',
    url='/artist/1'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='PMT',
    url='/organization/pmt'
)
dropdown_menu.addItem(item)

menu.addItem(dropdown_menu)

# Sign in Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Sign in'
dropdown_menu.icon = 'sign-in'
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

item = MenuItem(
    label='About',
    icon='info-circle',
    url='/about'
)
menu.addItem(item)

item = MenuItem(
    label='Contact',
    icon='envelope',
    url='/contact'
)
menu.addItem(item)


# Help Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Help'
dropdown_menu.icon = 'question-circle'
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
    