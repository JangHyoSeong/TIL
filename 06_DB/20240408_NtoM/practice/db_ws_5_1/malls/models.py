from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Customer(models.Model):
    name = models.TextField(max_length=100)
    product = models.ManyToManyField(Product)
    age = models.IntegerField()