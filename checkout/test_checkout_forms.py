"""
Testing checkout forms
"""

from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test the order form validators
    """

    def test_full_name_provided(self):
        """
        Test if full name is provided upon checkout
        """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_provided(self):
        """
        Test if email field is completed upon checkout
        """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_provided(self):
        """
        Test phone field is completed upon checkout
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_is_provided(self):
        """
        Test if country field is completed upon checkout
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_city_provided(self):
        """
        Test town or city is provided upon checkout
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'country': 'GB',
            'town_or_city': '',
            'street_address1': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address_completed(self):
        """
        Test if address is completed upon checkout
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': '',
            'town_or_city': 'test',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')
