from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_home_page_elements_are_correct(self):
        # User goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # User notices that the page title is "Talent Connection"
#         elem = self.get_element_by_tag_name('title')
        self.assertEqual(
            self.browser.title,
            'Talent Connection'
        )

        