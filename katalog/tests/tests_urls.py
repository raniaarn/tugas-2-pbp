from cgi import test
from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

class TestUrls(TestCase):

    def test_show_katalog_is_resolves(self):
        url = reverse('show_katalog')
        self.assertEquals(resolve(url).func, show_katalog)
