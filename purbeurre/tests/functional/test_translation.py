from django.test import TestCase, Client
from django.test import RequestFactory
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver



# Translations
class TraductionTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        base_dir = "/home/tashitsering/Documents/my staff/openclassrooms/OPEN_CLASS_PROJECT/Project_11_git"
        cls.selenium = WebDriver(executable_path=f"{base_dir}/geckodriver")
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_lang(self):
        for lang,h1_text in [('fr', 'Du gras, oui, mais de qualité !'),('en', 'Fat, yes, but of quality !')]:
            self.selenium.get("%s%s" % (self.live_server_url, "/{}".format(lang)))
            h1 = self.selenium.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)
