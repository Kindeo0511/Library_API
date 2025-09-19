from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from library.models import BookModel, UserModel, ReviewModel
from rest_framework_simplejwt.tokens import RefreshToken


class TestBookReview(APITestCase):

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

    
    
    def test_create_book_review(self):

        url = reverse('reviews-book', kwargs={'book_id': self.book.pk})
        data = {
            'user': self.user.pk,
            'book': self.book.pk,
            'rating': 1,
            'comment': 'create review comment'
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
