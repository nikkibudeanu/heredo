"""Bag Tests"""
from django.test import TestCase
from products.models import Product


class TestViews(TestCase):
    """
    Test views in bag app
    """
    def test_view_bag(self):
        """
        Test bag view
        """
        response = self.client.get('/bag/')
        self.assertTemplateUsed(response, 'bag/bag.html')
        self.assertEqual(response.status_code, 200)

    def test_add_to_bag(self):
        """
        Test if user can add to bag
        """
        product = Product.objects.create(
            name='Test Product',
            price='16.99',
            description='Test Description',
            image="Test image",
            rating='4.0',
            )
        response = self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})
        self.assertRedirects(response, f'/products/{product.id}/')

    def test_update_bag(self):
        """
        Test if user can update bag
        """
        product = Product.objects.create(
            name='Test Product',
            price='16.99',
            description='Test Description',
            image="Test image",
            rating='4.0',
            )
        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})
        response = self.client.post(f'/bag/update/{product.id}/', {
            'quantity': 3
            })
        bag = self.client.session['bag']
        self.assertEqual(bag['1'], 3)
        self.assertRedirects(response, '/bag/')

    def test_remove_item_from_bag(self):
        """
        Test if user can remove item from bag
        """
        product = Product.objects.create(
            name='Test Product',
            price='16.99',
            description='Test Description',
            image="Test image",
            rating='4.0',
            )
        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})

        response = self.client.get(f'/bag/remove/{product.id}/')
        bag = self.client.session['bag']

        self.assertEqual(bag, {})
        self.assertEqual(response.status_code, 200)
