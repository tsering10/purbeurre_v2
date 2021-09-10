from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from users.views import account as profile
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from purbeurre.forms import UserCreationForm
from selenium.webdriver.firefox.webdriver import WebDriver



class ProductSearchTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        base_dir = "/home/tashitsering/Documents/my staff/openclassrooms/OPEN_CLASS_PROJECT/Project_11_git/"
        cls.selenium = WebDriver(executable_path=f"{base_dir}/geckodriver")
        cls.selenium.implicitly_wait(10)
        cls.selenium.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_search_product(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        research_input = self.selenium.find_element_by_id("input_product")
        research_input.send_keys("Nutella")
        self.selenium.find_element_by_class_name("btn").click()
        
        






