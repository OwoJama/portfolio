from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomeTestPage(SimpleTestCase):
    def test_home_url(self):
        form = self.client.get('/')
        self.assertEqual(form.status_code, 200)

    def test_home_reverse(self):
        form = self.client.get(reverse('index'))
        self.assertEqual(form.status_code, 200)
