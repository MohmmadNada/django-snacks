from django.conf.urls import url
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnacksTest(SimpleTestCase):
    # Test that home and about url status codes
    def test_home_page_Status_code(self):
        url=reverse('home')
        actual_Status_code=self.client.get(url).status_code
        excepted_Status_code=200
        self.assertEqual(actual_Status_code,excepted_Status_code)
    def test_about_page_status(self):
        url=reverse('about')
        actual_status_code=self.client.get(url).status_code
        excepted_status_code=200
        self.assertEqual(actual_status_code,excepted_status_code)
    # Test home and about url template use, including ancestor template.
    def test_home_url_template(self):
        url=reverse('home')
        response=self.client.get(url)
        excepted='home.html'
        self.assertTemplateUsed(response,excepted)
    def test_about_url_template(self):
        url=reverse('about')
        response=self.client.get(url)
        excepted='about.html'
        self.assertTemplateUsed(response,excepted)