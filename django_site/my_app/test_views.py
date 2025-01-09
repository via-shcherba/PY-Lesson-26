from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import StandardUser


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/')
        self.assertTrue('vacancies' in response.context)

    def test_login_required(self):
        StandardUser.objects.create_user(username='test_user', email='test@test.com', password='test1234567')
        
        response = self.client.get('/create-vacancy/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test_user', password='test1234567')

        response = self.client.get('/create-vacancy/')
        self.assertEqual(response.status_code, 200)