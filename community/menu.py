from quinnrose.tools import Menu, MenuItem

# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

item = MenuItem(
    label='Home',
    url='/'
)
menu.addItem(item)

item = MenuItem(
    label='Post',
    url='/community/post'
)
menu.addItem(item)

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
    