from django.test import Client
from django.test import TestCase
from django.urls import reverse
from purbeurre.models import Products, Categories, Substitutes
from users.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class TestFavoritesView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="inconnu",
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )
        self.client.login(
            email="inconnu@gmail.com",
            password="1234AZERTY",
        )

    def test_display_saved_page(self):
        response = self.client.get(reverse("users:saved"))
        self.assertEqual(response.status_code, 200)

class PaginationTests(TestCase):
    def test_no_content_allow_empty_first_page(self):
        paginator = Paginator([], 2)
        self.assertEqual(paginator.validate_number(1), 1)