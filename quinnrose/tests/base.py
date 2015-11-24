import logging
from django.test import TestCase

class BaseTestCase(TestCase):

    logger = logging.getLogger('quinnrose.quinnrose.tests')
    
    def check_page_renders_correct_template(self, url_part, template_name):
        response = self.client.get(url_part)
        self.assertTemplateUsed(response, template_name)

