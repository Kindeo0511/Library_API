from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.request import Request
from rest_framework import status
from library.lib.services.book_service import get_book_by_id
from library.lib.services.book_review import create_review, get_review_by_id
from library.lib.serializers.serializer import ReviewSerializer, ReviewCreateSerializer
from rest_framework.permissions import IsAuthenticated
from library.models import BookModel  
from drf_yasg.utils import swagger_auto_schema

class CreateReviews(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(request_body=ReviewCreateSerializer, responses={201: ReviewSerializer})
    def post(self, request: Request, book_id:int) -> Response:
        serializer = ReviewCreateSerializer(data = request.data)

        if serializer.is_valid():
            book = get_book_by_id(book_id)
            book_review = create_review(serializer.validated_data, book, request.user)
            serializer = ReviewSerializer(book_review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, book_id: int) -> Response:
      
        reviews = get_review_by_id(book_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    
