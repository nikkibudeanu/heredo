"""Products Tests Models"""
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product


class TestProductsModels(TestCase):
    """
    Testing Category, Product models
    """
    def setUp(self):
        """
        Create test user, category, product.
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        product = Product.objects.create(
            name='Test Product Name',
            price='16.99',
            description='Test Description',
            rating='4.0',
        )

    def test_if_category_returns_friendly_name(self):
        """
        Test if category name is a string
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_if_product_returns_friendly_name(self):
        """
        Test model returns friendly name
        """
        product = Product.objects.get(name='Test Product Name')
        self.assertEqual((product.__str__()), product.name)
