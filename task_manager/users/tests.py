import unittest
from django.test import Client
from task_manager.users.models import User
import datetime


class UserCRUDTest(unittest.TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post('/users/create/', {'username': 'john',
                                                       'password': 'smith'})
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="john")
        self.assertEqual(user.date_joined, datetime.datetime(2024, 4, 19, 12,
                                                             15, 7, 145921,
                                                             tzinfo=datetime
                                                             .timezone.utc))

    def test_read(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="john")
        self.assertEqual(user.date_joined, datetime.datetime(2024, 4, 19, 12,
                                                             15, 7, 145921,
                                                             tzinfo=datetime
                                                             .timezone.utc))
