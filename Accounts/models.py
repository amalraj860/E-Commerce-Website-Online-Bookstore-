from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=25,null=True)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images')
    bio = models.CharField(max_length=200, null=True, blank=True)
    delivery_address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "user_data"
