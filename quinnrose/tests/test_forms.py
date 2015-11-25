from django import forms
from .base import BaseTestCase

class ContactPageTest(BaseTestCase):

    def test_page_loads_the_correct_form(self):
        self.check_page_renders_correct_template('/contact', 'home.html')

