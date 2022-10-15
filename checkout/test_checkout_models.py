"""Test Checkout Models"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order


class TestCheckoutModels(TestCase):
    """ Class to test the checkout Models """

    def setUp(self):
        """
        Set up test data
        """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com')
        testuser.save()

        Order.objects.create(
            order_number='987654321',
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def test_order_number(self):
        """
        Test the order number
        """
        order = Order.objects.get(email='test@test.com')
        self.assertEqual(str(order), order.order_number)
