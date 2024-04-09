from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Book(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField()
    genre = models.TextField()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_user = models.ManyToManyField(User, related_name='subscriber')
    nickname = models.TextField(max_length=20)