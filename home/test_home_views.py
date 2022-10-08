"""
Testing views in the Home app
"""
from django.test import TestCase
from django.contrib.messages import get_messages


class TestHomeViews(TestCase):


    def test_page_access(self):
        """
        Test the home view page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

