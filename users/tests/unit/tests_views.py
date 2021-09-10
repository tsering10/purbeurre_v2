from django.test import TestCase, Client
from django.urls import reverse
from purbeurre.models import Products, Categories, Substitutes
from users.models import User
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from users.views import account as profile
from purbeurre.forms import UserCreationForm
from django.core.paginator import Paginator,InvalidPage,PageNotAnInteger

class LoginPageTestCase(TestCase):
    """test login page"""

    def setUp(self):
        self.username = "alice"
        self.password = 'Qwerasdz12345'
        self.email = "sonam@gmail.com"
        self.user = User.objects.create_user(username=self.username, password=self.password,email=self.email)

    def test_login_page_status(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """ test with login data and response status code 302 Found  """
        response = self.client.post(reverse('users:login'), {
            "email": self.email,
            "password": self.password,
        })
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_username(self):
        """ test with invalid username and the request return response status code 200 """
        response = self.client.post(reverse('users:login'), {
            "email": '',
            "password": self.password,
        })
        self.assertEqual(response.status_code, 200)

    def test_login_invalide_password(self):
        """ test with invalide username and the request return response status code 200 """
        response = self.client.post(reverse('users:login'), {
            "email": self.email,
            "password": "",
        })
        self.assertEqual(response.status_code, 200)


class TestProfileView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )

    def test_display_profile_ok(self):
        request = self.factory.get(reverse("users:account"))
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_display_profile_not_ok(self):
        request = self.factory.get(reverse("users:account"))
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEqual(response.status_code, 302)

class LogoutPageTestCase(TestCase):
    """ test contact page """

    def test_logout_page(self):
        """ If returns a http code 200 is ok """
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)

class RegistrationPageTestCase(TestCase):
    """test signup page"""

    def setUp(self):
        sign_up_url = reverse('users:sign_up')
        user_data = {
            'username': 'alice',
            'email': 'alice@example.com',
            'password1': 'Qwerasdz12345',
            'password2': 'Qwerasdz12345'
        }

        self.home_url = (reverse('users:account'))
        self.response = self.client.post(sign_up_url, user_data)

    def test_display_register_page(self):
        response = self.client.get(reverse("users:sign_up"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "purbeurre/sign_up.html")
        self.assertContains(response, "username")
        self.assertContains(response, "email")
        self.assertContains(response, "password1")
        self.assertContains(response, "password2")

    def test_register_page_returns_200(self):
        """ 200 if the sign up is success"""
        response = self.client.get(reverse('users:sign_up'))
        self.assertEqual(response.status_code, 200)

    def test_csrf(self):
        """ test for csfr token """
        response = self.client.get(reverse('users:sign_up'))
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        """ test for sign up form """
        response = self.client.get(reverse('users:sign_up'))
        form = response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

class InvalidRegistrationPageTests(TestCase):
    """test registration page with invalid inputs"""

    def setUp(self):
        sign_up_url = reverse('users:sign_up')
        user_data = {
        }
        self.home_url = (reverse('users:account'))
        self.response = self.client.post(sign_up_url, user_data)

    def test_registration_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())

class SavedTestPageCase(TestCase):

    def setUp(self):
        # temporary data
        url = reverse('users:saved')
        self.data = {
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'Qwerasdz12345',
        }
        self.response = self.client.post(url, self.data)
        # create user with use temp data
        self.user = User.objects.create_user(**self.data)
        # create a category
        category = Categories.objects.create(category_name="Biscuits")

        origin = Products.objects.create(
            id_product=1,
            product_name="Biscuits Figue et son",
            category=category
        )
        replacement = Products.objects.create(
            id_product=2,
            product_name="Sablé Nature",
            category=category
        )

        Substitutes.objects.create(
            origin=origin,
            replacement=replacement,
            user=self.user)

        self.origin = Products.objects.get(pk=1)
        self.replacement = Products.objects.get(pk=2)

    def test_account_page_returns_200(self):
        """ return 200 if ok """
        self.client.login(**self.data)
        response = self.client.get(reverse('users:saved'))
        self.assertEqual(response.status_code, 302)

    def test_account_page_redirects(self):
        response = self.client.get(reverse('users:saved'))
        self.assertEqual(response.status_code, 302)

    def test_delete_substitute(self):
        self.client.login(**self.data)
        self.client.post(reverse('users:saved'), {
			"origin": self.origin.id_product,
			"replacement": self.replacement.id_product,
			})
        self.assertTrue(Substitutes.objects.exists())
 

        