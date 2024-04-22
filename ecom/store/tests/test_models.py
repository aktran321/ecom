from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')

    def test_string_representation(self):
        self.assertEqual(str(self.category), 'Electronics')

    def test_get_absolute_url(self):
        url = reverse('list-category', args=[self.category.slug])
        self.assertEqual(self.category.get_absolute_url(), url)

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            category=self.category,
            title='Smartphone',
            slug='smartphone',
            price=99.99
        )

    def test_string_representation(self):
        self.assertEqual(str(self.product), 'Smartphone')

    def test_get_absolute_url(self):
        url = reverse('product-info', args=[self.product.slug])
        self.assertEqual(self.product.get_absolute_url(), url)

    def test_price_field(self):
        self.assertEqual(self.product.price, 99.99)

    def test_foreign_key_relationship(self):
        self.assertEqual(self.product.category, self.category)
