from library.models import ReviewModel

def create_review(data, book, user):
    return ReviewModel.objects.create(**data, book=book, user=user)

def get_review_by_id(book_id):
    return ReviewModel.objects.filter(book_id=book_id)

