from django.test import TestCase
from django.test.client import Client
from accounts.models import Category


class ViewTest(TestCase):

    def test_home_status_code_and_template_used(self):
        client = Client()
        response = client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/home.html')

    def test_form_cant_register_new_transaction(self):
        pass
