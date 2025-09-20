from rest_framework import serializers
from library.models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'password', 'first_name', 'last_name']



class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
    required = True
)
    class Meta:
        model = BookModel
        fields = ['id','title', 'author', 'published_date']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['rating', 'comment']


    
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = ReviewModel
        fields = ['rating', 'comment', 'user', 'book']

