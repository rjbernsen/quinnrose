from .base import FunctionalTest
# from unittest import skip

class HomePageFunctionalityTest(FunctionalTest):

#     @skip('For now...')
    def test_base_page_elements_are_correct(self):
        
        # User goes to the home page
        self.browser.get(self.server_url)

        # User clicks on the "About" link and does not
        # get the error page
        self.browser.find_element_by_id('menu_about').click()
        self.check_for_page_not_found(self.browser.current_url, self.browser.page_source)
