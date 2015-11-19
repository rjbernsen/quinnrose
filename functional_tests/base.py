import sys
import os
import time
from datetime import datetime
from urllib.parse import urljoin
# from django.conf import settings
# from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
# from django.contrib.sessions.backends.db import SessionStore
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

DEFAULT_WAIT = 5
TEST_EMAIL = 'edith@mockmyid.com'
SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
##        self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome('C:\\DevelopmentWorkarea\\drivers\\chromedriver.exe')
        self.browser.implicitly_wait(DEFAULT_WAIT)

    def tearDown(self):
        if self._test_has_failed():
            if not os.path.exists(SCREEN_DUMP_LOCATION):
                os.makedirs(SCREEN_DUMP_LOCATION)
            for ix, handle in enumerate(self.browser.window_handles):
                self._windowid = ix
                self.browser.switch_to_window(handle)
                self.take_screenshot()
                self.dump_html()
        #-----------------------
        # This line is added to remove the
        # "An existing connection was forcibly closed by the remote host"
        # error from the output.
        # Found solution at https://github.com/django/django/pull/1806
        #-----------------------
        print('Refreshing the browser...')
        self.browser.refresh()
        #-----------------------
        self.browser.quit()
        super().tearDown()

    def check_static_file_exists(self, url_part):
        static_url = urljoin(self.server_url, url_part)
        self.browser.get(static_url)
        # Need to pause to let the url load.
        time.sleep(0.1)
#         print('{} source = {}'.format(static_url,self.browser.page_source))
        self.wait_for(
            lambda: self.assertNotIn(
                'not found on this server',
                self.browser.page_source,
                msg='Invalid Static URL: {}'.format(static_url)
            )
        )
        
    def get_element_by_tag_name(self, tag_name):
        self.wait_for_element_with_tag(tag_name)
        return self.browser.find_element_by_tag_name(tag_name)
    
    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id),
            'Could not find element with id {}. Page text was:\n{}'.format(
                element_id, self.browser.find_element_by_tag_name('body').text
            )
        )

    def wait_for_element_with_tag(self, tag_name):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(tag_name),
            'Could not find element with id {}. Page text was:\n{}'.format(
                tag_name, self.browser.find_element_by_tag_name('body').text
            )
        )

    def take_screenshot(self):
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.browser.get_screenshot_as_file(filename)
    
    def dump_html(self):
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f:
            f.write(self.browser.page_source)
    
    def _test_has_failed(self):
        for method, error in self._outcome.errors:
            if error:
                return True
        return False
    
    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}-window{windowid}-{timestamp}'.format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )
    
    def wait_for(self, function_with_assertion, timeout=DEFAULT_WAIT):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                return function_with_assertion()
            except (AssertionError, WebDriverException):
                time.sleep(0.1)

