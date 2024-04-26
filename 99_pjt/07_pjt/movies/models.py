from django.db import models

# Create your models here.
class actor(models.Model):
    name = models.CharField(max_length=100)
    
class movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField("actor", related_name='movies')

class review(models.Model):
    movie = models.ForeignKey("movie", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField() 