from django.test import TestCase
from katalog.models import CatalogItem

class KatalogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CatalogItem.objects.create(item_name = 'Tupperware', item_price=100000,
                                    item_stock= 2, description='anti ancur', rating=5,
                                    item_url='https://shopee.co.id/nanachen1994/3037215405')

    def test_item_name_label(self):
        katalog = CatalogItem.objects.get(id=1)
        field_label = katalog._meta.get_field('item_name').verbose_name
        self.assertEqual(field_label, 'item name')

    def test_item_name_max_length(self):
        katalog = CatalogItem.objects.get(id=1)
        max_length = katalog._meta.get_field('item_name').max_length
        self.assertEqual(max_length, 255)

    def test_item_price_label(self):
        katalog = CatalogItem.objects.get(id=1)
        field_label = katalog._meta.get_field('item_price').verbose_name
        self.assertEqual(field_label, 'item price')

    def test_item_stock_label(self):
        katalog = CatalogItem.objects.get(id=1)
        field_label = katalog._meta.get_field('item_stock').verbose_name
        self.assertEqual(field_label, 'item stock')

    def test_description_label(self):
        katalog = CatalogItem.objects.get(id=1)
        field_label = katalog._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_rating_label(self):
        katalog = CatalogItem.objects.get(id=1)
        field_label = katalog._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')