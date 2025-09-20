from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from library.models import BookModel, UserModel
from rest_framework_simplejwt.tokens import RefreshToken

class TestBooks(APITestCase):
    
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='bookadmin',
            password='securepass123',
            first_name='Book',
            last_name='Admin'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

        self.book_data = {
            'author': 'test',
            'title': 'test',
            'published_date': '2025-09-20'
        }
        self.book = BookModel.objects.create(**self.book_data)
    
    def test_create_book(self):
        self.url = reverse('create-book')
        self.data = {
            'author': 'test_author',
            'title': 'test_title',
            'published_date': '2025-09-20'
        }
        response = self.client.post(self.url, self.data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_list_book(self):
        self.url = reverse('list-book')
        
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1
    
    def test_get_book_by_id(self):
        url = reverse('get-book', kwargs={'book_id': self.book.pk})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == self.book.pk
        assert response.data['title'] == self.book.title
        assert response.data['author'] == self.book.author
        assert response.data['published_date'] == self.book.published_date
    
    def test_update_book_valid(self):
        url = reverse('update-book', kwargs={'book_id': self.book.pk})
        updated_data = {
            'title': 'update_author',
            'author': 'update_title',
            'published_date': '2024-01-01'
        }

        response = self.client.put(url, updated_data, format='json')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == updated_data['title']
        assert response.data['author'] == updated_data['author']
        assert response.data['published_date']  == updated_data['published_date']
    

    def test_delete_book(self):
        self.url = reverse('delete-book', kwargs={'book_id': self.book.pk})
        
        response = self.client.delete(self.url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert BookModel.objects.count() == 0
