from quinnrose.tools import Menu, MenuItem
from organization.temp_data import SOCIAL_LINKS

# Main Menu Items
# --------------------------------------
menu = Menu()
menu.right = True

# item = MenuItem(
#     label='About',
#     url='/organization/about'
# )
# menu.addItem(item)
# 
# dropdown_menu = Menu()
# dropdown_menu.label = 'Upcoming'
# dropdown_menu.is_dropdown = True
# # dropdown_menu.right = False
# 
# item = MenuItem(
#     label='Rocky Horror Show',
#     url='/organization/rocky'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='EDGES a song cycle',
#     url='/organization/edges'
# )
# dropdown_menu.addItem(item)
# 
# menu.addItem(dropdown_menu)
# 
# item = MenuItem(
#     label='Auditions',
#     url='/organization/auditions'
# )
# menu.addItem(item)
# 
# item = MenuItem(
#     label='Tickets',
#     url='/organization/tickets'
# )
# menu.addItem(item)
# 
# item = MenuItem(
#     label='Contact',
#     url='/organization/contact'
# )
# menu.addItem(item)
# 
# dropdown_menu = Menu()
# dropdown_menu.label = 'Social'
# dropdown_menu.is_dropdown = True
# dropdown_menu.foreign_object = SOCIAL_LINKS
# menu.addItem(dropdown_menu)

# item = MenuItem(
#     label='Blog',
#     url='/organization/blog'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Media',
#     url='/organization/media'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Facebook',
#     url='/organization/facebook'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Twitter',
#     url='/organization/twitter'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Google+',
#     url='/organization/googleplus'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='YouTube',
#     url='/organization/youtube'
# )
# dropdown_menu.addItem(item)
# 
# menu.addItem(dropdown_menu)

# # Account Dropdown
# # --------------------------------------
# dropdown_menu = Menu()
# dropdown_menu.label = 'My Org'
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
#     url='/organization/basicinfo'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Photos',
#     url='/organization/photos'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Events',
#     url='/organization/events'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Experience',
#     url='/organization/experience'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Training',
#     url='/organization/training'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Portfolio',
#     url='/organization/portfolio'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Biography',
#     url='/organization/biography'
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     separator=True
# )
# dropdown_menu.addItem(item)
# 
# item = MenuItem(
#     label='Preferences',
#     url='/organization/preferences'
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
    