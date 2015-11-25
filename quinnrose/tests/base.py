import logging
from django.test import TestCase
from django.test.client import RequestFactory

class BaseTestCase(TestCase):

    logger = logging.getLogger('quinnrose.quinnrose.tests')
    
    def setUp(self):
        # Every test needs access to the request factory.
        self.request_factory = RequestFactory()

    def check_page_renders_correct_template(self, url_part, template_name):
        response = self.client.get(url_part)
        self.assertTemplateUsed(response, template_name)

