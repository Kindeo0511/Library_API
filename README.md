# Library API project

A Django REST API for managing books, user authentication, and posting book reviews.



  Setup

1. Create a virtual environment and activate it
   
 On Windows: source venv\Scripts\activate
   
2. Install dependencies:
    pip install django djangorestframework djangorestframework-simplejwt drf-yasg pytest pytest-django

3. Run database migrations:
   python manage.py migrate

4. python manage.py runserver
5. Swagger API Documentation:
   http://localhost:8000/swagger/

   
API Endpoints

Authentication
* POST  auth/register/ – Register a new user
* POST  auth/login/ – Login and get JWT token
* POST  auth/refresh/ – Refresh JWT token
Books
* GET books/ – List all books
* POST books/create – Create book 
* GET books/{id}/ – Retrieve a single book
* PUT books/update/{id}/ – Update book 
* DELETE books/update/{id}/ – Delete bo
Reviews
* GET/POST   books/{id}/reviews/ – List reviews for a book and create a review



