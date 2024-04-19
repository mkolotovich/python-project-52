import unittest
from django.test import Client
from task_manager.tasks.models import Task


class TasksCRUDTest(unittest.TestCase):
    fixtures = ['tasks.json']

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post('/tasks/create/', {'name': 'tota',
                                                       'status': 1})
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(name="tota")
        self.assertEqual(task.status.id, 1)

    def test_read(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(name="tota")
        self.assertEqual(task.status.id, 1)
