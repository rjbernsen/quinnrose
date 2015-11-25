from .base import FunctionalTest
from quinnrose.config import FULL_SITE_NAME
from unittest import skip

@skip('Just because...')
class LayoutAndStylingTest(FunctionalTest):

#     @skip('For now...')
    def test_base_page_elements_are_correct(self):
        # User goes to the home page
        self.browser.get(self.server_url)

        # User notices that the page title is "Talent Connection"
        self.assertEqual(
            self.browser.title,
            FULL_SITE_NAME
        )

    def test_base_page_static_files_exist(self):
        self.browser.get(self.server_url)
#         self.wait_for_element_with_tag('link')
        css_files = self.browser.find_elements_by_tag_name('link')
        css_list = [the_url.get_attribute('href') for the_url in css_files]

        js_files = self.browser.find_elements_by_tag_name('script')
        js_list = [the_url.get_attribute('src') for the_url in js_files]

        img_files = self.browser.find_elements_by_tag_name('img')
        img_list = [the_url.get_attribute('src') for the_url in img_files]

        for css_url in css_list:
            if css_url != None:
#                 self.logger.info('css_url = {}'.format(css_url))
                self.check_static_file_exists(css_url)
 
#         print('js_list = {}'.format(js_list))
        for js_url in js_list:
            if js_url != None and len(js_url) > 0:
#                 self.logger.info('js_url = {}'.format(js_url))
                self.check_static_file_exists(js_url)
 
        for img_url in img_list:
            if img_url != None:
#                 self.logger.info('img_url = {}'.format(img_url))
                self.check_static_file_exists(img_url)
 
