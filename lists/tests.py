from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from lists.views import Home

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, Home)