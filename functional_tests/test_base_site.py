from .base import FunctionalTest
from unittest import skip

class HomePageFunctionalityTest(FunctionalTest):

    @skip('For now...')
    def test_base_page_elements_are_correct(self):
        
        # User goes to the home page
        self.browser.get(self.server_url)

        # User clicks on the "About" link and does not
        # get the error page
        self.browser.find_element_by_id('menu_about').click()
        self.check_for_page_not_found(self.browser.current_url, self.browser.page_source)
        
        # User returns to the home page and clicks on
        # the "Privacy" link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('link_privacy').click()
        self.check_for_page_not_found(self.browser.current_url, self.browser.page_source)
        
        # User returns to the home page and clicks on
        # the "Terms" link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('link_terms').click()
        self.check_for_page_not_found(self.browser.current_url, self.browser.page_source)
        

class AboutPageFunctionalityTest(FunctionalTest):

    def check_active_about_link(self, link_id):
        elem = self.browser.find_element_by_id(link_id)
        class_list = elem.get_attribute('class').split(' ')
        
        self.wait_for(
            lambda: self.assertIn('active', class_list)
        )
        
    @skip('For now...')
    def test_base_page_elements_are_correct(self):
        
        # User goes to the home page and clicks on
        # the "About" link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('menu_about').click()

        # The first item in the list is active
        self.check_active_about_link('about_the_site')
       
        # The second item is clicked and becomes active
        self.check_active_about_link('about_core_values')
        
        # The third item is clicked and becomes active
        self.check_active_about_link('about_mission_statement')
        
        # The fourth item is clicked and becomes active
        self.check_active_about_link('about_we_do')
        
        # The fifth item is clicked and becomes active
        self.check_active_about_link('about_we_dont')
        
class ContactPageFunctionalityTest(FunctionalTest):

#     @skip('For now...')
    def test_base_page_elements_are_correct(self):
        
        # User goes to the home page and clicks on
        # the "Contact" link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('menu_contact').click()
        self.check_for_page_not_found('/contact', self.browser.page_source)
        
        
