from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from library.models import BookModel, UserModel, ReviewModel
from rest_framework_simplejwt.tokens import RefreshToken


class TestBookReview(APITestCase):

    def setUp(self): 

        self.user_data = {
            'username': 'bookadmin',
            'password':'securepass123',
            'first_name': 'Book',
            'last_name': 'Admin'
        }
       
        self.user = UserModel.objects.create_user(**self.user_data)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')


        self.book_data = {
            'author': 'test',
            'title': 'test',
            'published_date': '2025-09-20'
        }

        self.book = BookModel.objects.create(**self.book_data)

    
    
    def test_create_book_review(self):

        url = reverse('reviews-book', kwargs={'book_id': self.book.pk})
        data = {
            'user': self.user.pk,
            'book': self.book.pk,
            'rating': 1,
            'comment': 'create review comments'
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['user']['username'] == self.user.username
        assert response.data['user']['first_name'] == self.user.first_name
        assert response.data['user']['last_name'] == self.user.last_name
        assert response.data['book']['author'] == self.book.author
        assert response.data['book']['title'] == self.book.title
        assert response.data['book']['published_date'] == self.book.published_date
        assert response.data['rating'] == data['rating']
        assert response.data['comment'] == data['comment']

