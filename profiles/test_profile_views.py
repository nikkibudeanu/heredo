"""Profiles Test Views"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from checkout.models import Order
from profiles.models import UserProfile


class TestProfilesView(TestCase):
    """ Class to test the profiles views """

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
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def test_profile_template(self):
        """
        Test if the template is correct
        """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_url(self):
        """
        Test if logged in user can access their profile page
        """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get('/profiles/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_get_order_detail_page(self):
        """
        Test if user can see their order history
        """
        self.client.login(username='test_user1', password='test_password')
        test_user = User.objects.get(username='test_user')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get('/profiles/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
