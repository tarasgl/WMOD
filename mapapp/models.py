from django.db import models
from location_field.models.plain import PlainLocationField
from django.core.validators import URLValidator

# Create your models here.
class Icon(models.Model):
    iconImage = models.ImageField(upload_to='', blank=True, null=True)
    iconType = models.CharField(max_length=80, blank=True, null=True)
    def __str__(self):
        return self.iconType


class Marker(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    city = models.CharField(max_length=255)
    location = PlainLocationField(zoom=7,default='49.842728, 24.025021')
    image = models.ImageField(upload_to='', blank=True, null=True)
    icon = models.ForeignKey(Icon, blank=True, null=True)

    def __str__(self):
        return self.title

class Carousel(models.Model):
  name = models.ForeignKey(Marker, blank=True, null=True)
  def __str__(self):
      return str(self.name)
