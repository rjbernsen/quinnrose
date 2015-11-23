class Featurette(object):
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
    
    def __init__(self):
        
        self.title = None
        self.sub_title = None
        self.description = None
        
        self.image_file_name = None

featurettes = []

# Number 1
# --------------------------------------
featurette = Featurette()
featurette.title = "Featurette #1"
featurette.sub_title = "Featurette subtitle #1"
featurette.description = 'Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'
featurette.image_file_name = 'carousel-06.jpg'
featurettes.append(featurette)

# Number 2
# --------------------------------------
featurette = Featurette()
featurette.title = "Featurette #2"
featurette.sub_title = "Featurette subtitle #2"
featurette.description = 'Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'
featurette.image_file_name = 'carousel-07.jpg'
featurettes.append(featurette)

# Number 3
# --------------------------------------
featurette = Featurette()
featurette.title = "Featurette #3"
featurette.sub_title = "Featurette subtitle #3"
featurette.description = 'Donec ullamcorper nulla non metus auctor fringilla. Vestibulum id ligula porta felis euismod semper. Praesent commodo cursus magna, vel scelerisque nisl consectetur. Fusce dapibus, tellus ac cursus commodo.'
featurette.image_file_name = 'carousel-08.jpg'
featurettes.append(featurette)

if __name__ == "__main__":
    print(featurettes)
    