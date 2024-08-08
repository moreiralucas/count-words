from django.test import TestCase, Client
from django.urls import reverse
from core.forms import TextForm

class TextFormViewTests(TestCase):
    def setUp(self):
        self.url = reverse("text_form")
        self.client = Client()

    def test_form_valid_input(self):
        data = {"text": "This is a test."}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Number of words:")
        self.assertContains(response, "4")

    def test_form_invalid_input(self):
        data = {"text": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertTrue(form.errors)
        self.assertIn("text", form.errors)
