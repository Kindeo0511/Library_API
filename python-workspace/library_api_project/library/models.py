from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserModel(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    
    def __str__(self):
        return f"{self.title} {self.author}"

class ReviewModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} rated  '{self.book.title}' {self.rating}/5"