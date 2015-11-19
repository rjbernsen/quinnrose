from .base import BaseTestCase

class HomePageTest(BaseTestCase):

    def test_page_renders_correct_template(self):
        self.check_page_renders_correct_template('/', 'home.html')

 