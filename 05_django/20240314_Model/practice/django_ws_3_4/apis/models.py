from django.db import models

# Create your models here.
class APIInfo(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    api_url  = models.URLField()
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    sample_data = models.JSONField()
    created_at = models.DateTimeField()