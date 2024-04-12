import unittest
from django.test import Client
from task_manager.users.models import User


class UserCRUDTest(unittest.TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post('/users/create/', {'username': 'john',
                                                       'password': 'smith'})
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="john")
        self.assertEqual(user.password, 'smith')

    def test_read(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="john")
        self.assertEqual(user.password, 'smith')
