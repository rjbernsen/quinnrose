from quinnrose.tools import Menu, MenuItem

# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

# item = MenuItem(
#     label='My Profile',
#     url='/artist/profile'
# )
# menu.addItem(item)
# 
# item = MenuItem(
#     label='Auditions',
#     url='/artist/auditions'
# )
# menu.addItem(item)
# 
# # Membership Dropdown
# # --------------------------------------
# dropdown_menu = Menu()
# dropdown_menu.label = 'Shannon'
# dropdown_menu.is_dropdown = True
# # dropdown_menu.right = True
# 
# item = MenuItem(
#     label='Sign in',
#     url='/signin'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Sign out',
#     url='/signin/signout'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     separator=True
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='My Account'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Basic info',
#     url='/artist/basicinfo'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Photos',
#     url='/artist/photos'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Skills',
#     url='/artist/skills'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Experience',
#     url='/artist/experience'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Training',
#     url='/artist/training'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Portfolio',
#     url='/artist/portfolio'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Biography',
#     url='/artist/biography'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     separator=True
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Settings',
#     url='/artist/settings'
# )
# dropdown_menu.addItem(item)
# 
# menu.addItem(dropdown_menu)

# Help Dropdown
# --------------------------------------
dropdown_menu = Menu()
dropdown_menu.label = 'Help'
dropdown_menu.icon = 'question'
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
    