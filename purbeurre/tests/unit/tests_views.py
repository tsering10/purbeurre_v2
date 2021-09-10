from django.test import TestCase, Client
from django.urls import reverse
from purbeurre.models import Products, Categories, Substitutes
from users.models import User
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from users.views import account as profile
from purbeurre.forms import UserCreationForm


class IndexPageTestCase(TestCase):

    # test that index returns a 200
    # must start with `test`
    def test_index_page(self):
        # you must add a name to index view: `name="index"`
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class LegalPageTestCase(TestCase):
    """ test legal page """

    def test_legals_page(self):
        """ If returns a http code 200 is ok """
        response = self.client.get(reverse('purbeurre:legal'))
        self.assertEqual(response.status_code, 200)


class ContactsPageTestCase(TestCase):
    """ test contact page """

    def test_contacts_page(self):
        """ If returns a http code 200 is ok """
        response = self.client.get(reverse('purbeurre:contacts'))
        self.assertEqual(response.status_code, 200)

class DetailPageTestCase(TestCase):
    """ test product detail page """

    def setUp(self):
        """ create testing product """
        category = Categories.objects.create(category_name="Pâte à tartiner")
        nutella = Products.objects.create(
            id_product=1,
            product_name="nutella",
            category=category
        )
        self.product = Products.objects.get(product_name="nutella")

    def test_detail_page_returns_200(self):
        """ returns status_code 200 if the page is ok """
        product_id = self.product.id_product
        response = self.client.get(reverse('purbeurre:product_detail', args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_404(self):
        """ return 404 if the query is invalid """
        product_id = self.product.id_product + 1
        response = self.client.get(reverse('purbeurre:product_detail', args=(product_id,)))
        self.assertEqual(response.status_code, 404)

class SearchPageTestCase(TestCase):
    def setUp(self):
        category = Categories.objects.create(category_name="Pâte à tartiner")
        Products.objects.create(
            id_product=1,
            product_name="Nocilla",
            category=category,
            nutrition_score="d"
        )

        Products.objects.create(
            id_product=2,
            product_name="Nocciolata",
            category=category,
            nutrition_score="a"
        )
        self.password = "Qwerasdz12345"
        self.user = User.objects.create_user(
            username="alice",
            password=self.password,
            email="alice@example.com"
        )
        self.client = Client()
        self.origin = Products.objects.get(pk=1)
        self.replacement = Products.objects.get(pk=2)
        self.client.force_login(user=self.user)

    def test_search_page_returns_200(self):
        """ returns 200 if the query parameters are correct """
        response = self.client.get(reverse('purbeurre:search'), {"query": "Nocilla"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Nocilla', response.content)

    def test_random_list_of_products_if_no_query(self):
        # Test that an empty query returns to a page displaying a certain message and suggests products
        response = self.client.get(
            reverse('purbeurre:search'), {"query": ""}

        )
        self.assertIn(b'Suggestion de produits', response.content)
