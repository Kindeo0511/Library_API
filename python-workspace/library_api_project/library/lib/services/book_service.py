from library.models import BookModel
from django.shortcuts import get_object_or_404



def get_all_books():
    return BookModel.objects.all()

def create_book(data):
    return BookModel.objects.create(**data)

def get_book_by_id(book_id):
    return  get_object_or_404(BookModel, id=book_id)

def update_book(book, data):
    for field, value in data.items():
        setattr(book, field, value)
    book.save()  
    return book

def delete_book(book):
    book.delete()



