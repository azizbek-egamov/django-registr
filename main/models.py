from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    avtor = models.CharField(max_length=255)
    narx = models.IntegerField()
    rasm = models.FileField(upload_to='photo')