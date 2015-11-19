from django.test import TestCase
# from django.contrib.staticfiles.storage import staticfiles_storage #The file storage engine to use when collecting static files with the collectstatic management command.
# from django.contrib.staticfiles import finders

class BaseTestCase(TestCase):

    def check_page_renders_correct_template(self, url_part, template_name):
        response = self.client.get(url_part)
        self.assertTemplateUsed(response, template_name)

