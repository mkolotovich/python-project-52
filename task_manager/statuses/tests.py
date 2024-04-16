import unittest
from django.test import Client
from task_manager.statuses.models import Status
import datetime


class StatusCRUDTest(unittest.TestCase):
    fixtures = ['statuses.json']

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post('/statuses/create/', {'name': 'новый1'})
        self.assertEqual(response.status_code, 302)
        status = Status.objects.get(name="новый1")
        self.assertEqual(status.created_at, datetime.datetime(2024, 4, 15, 11,
                                                              52, 48, 278782,
                                                              tzinfo=datetime
                                                              .timezone.utc))

    def test_read(self):
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 302)
        status = Status.objects.get(name="новый1")
        self.assertEqual(status.created_at, datetime.datetime(2024, 4, 15, 11,
                                                              52, 48, 278782,
                                                              tzinfo=datetime
                                                              .timezone.utc))

    def test_update(self):
        response = self.client.post('/statuses/2/update/', {'name': 'новый2'})
        self.assertEqual(response.status_code, 302)
        status = Status.objects.get(name="новый2")
        self.assertTrue(status.created_at)

