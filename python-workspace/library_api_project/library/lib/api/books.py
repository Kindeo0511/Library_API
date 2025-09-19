from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.request import Request
from rest_framework import status
from library.lib.services.book_service import create_book, get_book_by_id, update_book, delete_book, get_all_books
from library.lib.serializers.serializer import BookSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema





class BookList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        books = get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateBook(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BookSerializer, responses={201: BookSerializer})
    def post(self, request: Request) -> Response:
        serializer  = BookSerializer(data = request.data)

        if serializer.is_valid():
            book = create_book(serializer.validated_data)           
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetBookById(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, book_id:int) -> Response:

        BookModel = get_book_by_id(book_id)
        serializer = BookSerializer(BookModel)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UpdateBook(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=BookSerializer, responses={201: BookSerializer})
    def put(self,request, book_id:int) -> Response:
        book = get_book_by_id(book_id)
        serializer = BookSerializer(book, data = request.data)

        if serializer.is_valid():
            update = update_book(book, serializer.validated_data)
            return Response(BookSerializer(update).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request, book_id: int) -> Response:
        book = get_book_by_id(book_id)
        serializer = BookSerializer(book, data = request.data, partial=True)

        if serializer.is_valid ():
            update = update_book(book, serializer.validated_data)
            return Response (BookSerializer(update).data, status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteBook(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, book_id:int) -> Response:
        book = get_book_by_id(book_id)
        delete_book(book)
        return Response(status=status.HTTP_204_NO_CONTENT)
