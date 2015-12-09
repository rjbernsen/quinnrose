from quinnrose.tools import Menu, MenuItem

# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

item = MenuItem(
    label='Profile',
    url='/artists/profile'
)
menu.addItem(item)

item = MenuItem(
    label='Auditions',
    url='/artists/auditions'
)
menu.addItem(item)

# Membership Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Shannon'
dropdown_menu.is_dropdown = True
dropdown_menu.right = True

item = MenuItem(
    label='Sign in',
    url='/signin'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Sign out',
    url='/signin/signout'
)
dropdown_menu.addItem(item)

item = MenuItem(
    separator=True
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='My Account'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Basic info',
    url='/artists/basicinfo'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Photos',
    url='/artists/photos'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Skills',
    url='/artists/skills'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Experience',
    url='/artists/experience'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Training',
    url='/artists/training'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Portfolio',
    url='/artists/portfolio'
)
dropdown_menu.addItem(item)

item = MenuItem(
    label='Biography',
    url='/artists/biiography'
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
    