from quinnrose.tools import HomePageInfoItem

home_page_info = []

# Number 1
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Artists"
info_item.description = 'Everyone who has any kind of artistic talent should have an opportunity to share their gifts. We make opportunities happen by giving talented folks a place to "get the word" out and be noticed.'
info_item.link = 'subscribe/artist'
info_item.icon = 'user'
home_page_info.append(info_item)

# Number 2
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Organizations"
info_item.description = 'Any group that regularly - or even occasionally - requires people with artistic talents for any type of even can find the exact person for every need. Need a performer with an unusual skill? Find them here!'
info_item.link = 'subscribe/organization'
info_item.icon = 'users'
home_page_info.append(info_item)

# Number 3
# --------------------------------------
info_item = HomePageInfoItem()
info_item.title = "Community"
info_item.description = 'Bringing talented people and arts organizations together is the primary goal of every part of the this site. We can help you make those connections. Subscribe to get started!'
info_item.link = 'community'
info_item.icon = 'share-alt'
home_page_info.append(info_item)

if __name__ == "__main__":
    print(home_page_info)
    