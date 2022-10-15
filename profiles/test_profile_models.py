"""Profiles Test Models"""
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestProfileModels(TestCase):
    """
    Class for testing the profile model
    """
    def setUp(self):
        """
        Create a test user
        """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com')
        testuser.save()

    def test_profile_username(self):
        """
        Test if username is correct
        """
        testuser = User.objects.get(username='test_user')
        profile = UserProfile.objects.get(user=testuser)
        self.assertEqual(str(profile), profile.user.username)
