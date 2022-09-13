from django.test import TestCase, Client
from katalog.models import CatalogItem

class AppTest(TestCase):
    def test_katalog_url_exists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)
    def test_katalog_using_template(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')

class AppModelTest(TestCase):
    def setup(self):
        self.item1 = CatalogItem.objects.create(
            item_name = "Milk",
            item_price = 26450,
            item_stock = 50,
            description = "Fresh",
            rating = 5,
            item_url = "https://www.tokopedia.com/deposusuaa/milk-life-1l-mocha-lactose-free-milk-susu-milklife-bebas-laktosa-kopi-pure-fresh-milk?extParam=ivf%3Dfalse&src=topads",
        )
