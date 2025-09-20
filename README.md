# Library API project

A Django REST API for managing books, user authentication, and posting book reviews.



  Setup

1. Create a virtual environment and activate it
   
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
2. Install dependencies:
    pip install django djangorestframework djangorestframework-simplejwt drf-yasg pytest pytest-django

3. Run database migrations:
   python manage.py migrate

4. python manage.py runserver
5. Swagger API Documentation:
   http://localhost:8000/swagger/

   
Authentication Required

For protected endpoints, include this header:
Authorization: Bearer <your-access-token>

POST /auth/login/ — Obtain JWT Token

Request:

{
  "username": "your_username",
  "password": "your_password"
}


Response:

{
  "access": "your-access-token",
  "refresh": "your-refresh-token"

  OST /auth/register/ — Register New User

Request:

{
  "username": "test",
  "password": "test",
  "first_name": "test",
  "last_name": "test"
}
Response:

{
  "id": 1,
  "username": "test",
  "first_name": "test",
  "last_name": "test"
}

Book Endpoints

GET /api/books/ — Get All Books

Response:

[

  "id": 1,
  "title": "test",
  "author": "test",
  "published_date": "2025-09-19"

]

POST /api/books/create/ — Add a New Book

Request:

{
  "title": "New Book",
  "author": "New Author",
  "published_date": "2025-01-01"
}
Response:

{
  "id": 2,
  "title": "New Book",
  "author": "New Author",
  "published_date": "2025-01-01"
}

GET /api/books/<book_id>/ — Get Book by ID

Response:

{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "published_date": "2023-01-01"
}

PUT /api/books/update/<book_id>/ — Update a Book

Request:

{
  "title": "Updated Title",
  "author": "Updated Author",
  "published_date": "2025-01-01"
}


Response:

{
  "id": 1,
  "title": "Updated Title",
  "author": "Updated Author",
  "published_date": "2025-01-01"
}

DELETE /api/books/delete/<book_id>/ — Delete a Book

Response:

204 No Content


Review Endpoint

POST /books/<book_id>/reviews/ — Create a Review for a Book

Request:

{
  "rating": 5,
  "comment": "This book was amazing!"
}


Response:

{
  "id": 1,
  "book": 1,
  "rating": 5,
  "comment": "This book was amazing!"
}


