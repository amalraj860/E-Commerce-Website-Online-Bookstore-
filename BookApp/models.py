from django.db import models
from Accounts.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, blank=True)
    follow_author = models.CharField(max_length=2083, blank=True)
    book_available = models.BooleanField()
    category = models.CharField(max_length=2083, blank=True)

    class Meta:
        db_table ='db_book'


# models for cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table ='db_cart'




