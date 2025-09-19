from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from library.models import UserModel

class TestUser(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'testfirstname',
            'last_name': 'testlastname'
        }
        self.user = UserModel.objects.create(**self.user_data) 
  
    def test_user_registration(self):
        self.url = reverse('auth-register')
        self.data = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test'
        }
        response = self.client.post(self.url, self.data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_user_registration_invalid(self):
        self.url = reverse('auth-register')
        self.data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test'
        }
        response = self.client.post(self.url, self.data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_user_login(self):

        UserModel.objects.create_user(
            username='loginuser',
            password='pass123',
            first_name='kindeo',
            last_name='nikdo'
        )

        self.url = reverse('auth-login')
        data = {
            'username': 'loginuser',
            'password': 'pass123'
        }

        response = self.client.post(self.url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data
        
    def test_user_invalid_login(self):
        UserModel.objects.create_user(
        username='loginuser',
        password='pass123',
        first_name='kindeo',
        last_name='nikdo'
    )

        self.url = reverse('auth-login')
        data = {
            'username': 'loginuser',
            'password': 'wrongpassword'
        }

        response = self.client.post(self.url, data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'access' not in response.data
        assert 'refresh' not in response.data

 

