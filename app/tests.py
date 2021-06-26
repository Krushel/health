from django.test import TestCase

# Create your tests here.

from django.urls import reverse

class HealthViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/health/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('health'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('health'))
        self.assertEqual(resp.content, 'healthy')
