from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from library.lib.api.views import RegisterUser
from library.lib.api.books import *
from library.lib.api.review import CreateReviews
from library.lib.api.swagger import schema_view

urlpatterns = [
    path('auth/register/', RegisterUser.as_view(), name='auth-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth-login'),

    path('books/', BookList.as_view(), name='list-book'),
    path('books/create/', CreateBook.as_view(), name='create-book'),
    path('books/<int:book_id>/', GetBookById.as_view(), name='get-book'),
    path('books/update/<int:book_id>/', UpdateBook.as_view(), name='update-book'),
    path('books/delete/<int:book_id>/', DeleteBook.as_view(), name='delete-book'),
    path('books/<int:book_id>/reviews/', CreateReviews.as_view(), name='reviews-book'),
    
]


