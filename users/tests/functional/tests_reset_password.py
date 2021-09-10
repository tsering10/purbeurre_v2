from django.test import TestCase, Client
from django.urls import reverse
from purbeurre.models import Products, Categories, Substitutes
from users.models import User
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from users.views import account as profile



class TestPasswordRestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_display_password_reset_page(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/password_reset.html")
        self.assertContains(response, "email")

    def test_display_password_reset_done_page_ok(self):
        response = self.client.get(reverse("password_reset_done"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/password_reset_done.html")

    def test_display_password_reset_complete_page_ok(self):
        response = self.client.get(reverse("password_reset_complete"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/password_reset_complete.html")

    def test_display_password_reset_done_page_not_ok(self):
        request = self.factory.get(reverse("password_reset_done"))
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEqual(response.status_code, 302)

    def test_display_password_reset_complete_page_not_ok(self):
        request = self.factory.get(reverse("password_reset_complete"))
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEqual(response.status_code, 302)
