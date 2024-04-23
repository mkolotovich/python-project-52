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
        self.assertEqual(task.status.id, 6)

    def test_read(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(name="tota")
        self.assertEqual(task.status.id, 6)

    def test_read_filters(self):
        response = self.client.get('/tasks/?status=6')
        self.assertEqual(response.status_code, 302)
        tasks = Task.objects.all().filter(status_id=6)
        self.assertEqual(len(tasks), 1)
