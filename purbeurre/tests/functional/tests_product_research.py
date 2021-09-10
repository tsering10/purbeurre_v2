from django.test import TestCase, Client
from django.urls import reverse
from purbeurre.models import Products, Categories, Substitutes
from users.models import User
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from users.views import account as profile
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from purbeurre.forms import UserCreationForm
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class ProductSearchTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        base_dir = "/home/tashitsering/Documents/my staff/openclassrooms/OPEN_CLASS_PROJECT/Project_11_git/"
        cls.selenium = WebDriver(executable_path=f"{base_dir}/geckodriver")
        cls.selenium.implicitly_wait(50)
        cls.selenium.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_search_product(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        search_product = self.selenium.find_element_by_id('input_product')
        # submit = self.selenium.find_element_by_id('submit_button')
        # # populate the form with data
        # search_product.send_keys('nutella')

        # # submit form
        # submit.click()

        # check result; page source looks at entire html document
        # assert 'Biscuits aux pépites de chocolat' in self.selenium.page_source









