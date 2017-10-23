from django.db import models
from location_field.models.plain import PlainLocationField
from django.core.validators import URLValidator

# Create your models here.
class Marker(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    city = models.CharField(max_length=255)
    location = PlainLocationField(zoom=7)
    image = models.ImageField(upload_to='', blank=True, null=True)
    link = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.title
