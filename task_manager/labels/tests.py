import unittest
from django.test import Client
from task_manager.labels.models import Label


class LabelsCRUDTest(unittest.TestCase):
    fixtures = ['labels.json']

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post('/labels/create/', {'name': 'bug1'})
        self.assertEqual(response.status_code, 302)
        label = Label.objects.get(name="bug1")
        self.assertEqual(label.name, "bug1")

    def test_read(self):
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 302)
        label = Label.objects.get(name="bug1")
        self.assertEqual(label.id, 3)

    def test_delete(self):
        response = self.client.post('/labels/delete/3/')
        self.assertEqual(response.status_code, 404)
        label = Label.objects.get(name="bug1")
        self.assertEqual(label.name, "bug1")
