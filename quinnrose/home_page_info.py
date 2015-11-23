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
    
home_page_info = []

# Number 1
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Key Point #1"
info_item.description = 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.'
info_item.link = '1'
home_page_info.append(info_item)

# Number 2
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Key Point #2"
info_item.description = 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.'
info_item.link = '2'
home_page_info.append(info_item)

# Number 3
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Key Point #3"
info_item.description = 'Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.'
info_item.link = '3'
home_page_info.append(info_item)

if __name__ == "__main__":
    print(home_page_info)
    