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
        self.user = UserModel.objects.create_user(**self.user_data) 
  
        self.login_url = reverse('auth-login')
        self.register_url =  reverse('auth-register')

    def test_user_registration(self):
        data = {
            'username': 'test',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'test'
        }
        response = self.client.post(self.register_url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_user_registration_invalid(self):
        data = {
            'first_name': 'test',
            'last_name': 'test'
        }
        response = self.client.post(self.register_url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_user_login(self):

        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = self.client.post(self.login_url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data
        
    def test_user_invalid_login(self):
        data = {
            'username': 'loginuser',
            'password': 'wrongpassword'
        }

        response = self.client.post(self.login_url, data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'access' not in response.data
        assert 'refresh' not in response.data

 

