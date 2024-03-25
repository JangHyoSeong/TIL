from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.TextField(max_length = 13)
    author = models.TextField()
    title = models.TextField()
    pubDate = models.DateField()
    description = models.TextField()
    pricesales = models.IntegerField()
    stockstatus = models.TextField()
    adult = models.BooleanField()