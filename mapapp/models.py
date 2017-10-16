from django.db import models

# Create your models here.
class Marker(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    
