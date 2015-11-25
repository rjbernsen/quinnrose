from quinnrose.tests.base import BaseTestCase
from quinnrose.menus import menu
from quinnrose.home_page_info import home_page_info
from quinnrose.featurettes import featurettes

class HomePageTest(BaseTestCase):

    def test_page_renders_correct_template(self):
        self.check_page_renders_correct_template('/', 'home.html')

    def test_page_includes_menu_object(self):
        response = self.client.get('/')
        self.assertEqual(response.context['menu'], menu)
        
    def test_page_includes_carousel_images(self):
        response = self.client.get('/')
        self.assertTrue(len(response.context['carousel_images']) > 0)
        
    def test_page_includes_home_page_info(self):
        response = self.client.get('/')
        self.assertEqual(response.context['home_page_info'], home_page_info)
        
    def test_page_includes_featurettes(self):
        response = self.client.get('/')
        self.assertEqual(response.context['featurettes'], featurettes)
        
class HomeSubPagesTest(BaseTestCase):

    def test_page_renders_correct_template(self):
#         self.check_page_renders_correct_template('/about', 'about.html')
        self.check_page_renders_correct_template('/privacy', 'privacy.html')
        self.check_page_renders_correct_template('/terms', 'terms.html')

class AboutPageTest(BaseTestCase):
    
    def test_page_renders_correct_template(self):
        self.check_page_renders_correct_template('/about',   'about_the_site.html')
        self.check_page_renders_correct_template('/about/1', 'about_the_site.html')
        self.check_page_renders_correct_template('/about/2', 'about_core_values.html')
        self.check_page_renders_correct_template('/about/3', 'about_mission_statement.html')
        self.check_page_renders_correct_template('/about/4', 'about_we_do.html')
        self.check_page_renders_correct_template('/about/5', 'about_we_dont.html')
