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
    location = PlainLocationField(zoom=7)
    image = models.ImageField(upload_to='', blank=True, null=True)
    link = models.TextField(validators=[URLValidator()])
    icon = models.ForeignKey(Icon, blank=True, null=True)
    #ICON_CHOICES = (
        #('https://image.flaticon.com/icons/svg/89/89013.svg', 'church'),
        #('https://image.flaticon.com/icons/svg/46/46564.svg' , 'park'),
        #('https://image.flaticon.com/icons/svg/8/8913.svg', 'museum'),
        #('https://image.flaticon.com/icons/svg/1/1160.svg','monument'),
        #('https://image.flaticon.com/icons/svg/77/77358.svg' , 'theatre'),
        #('https://image.flaticon.com/icons/svg/0/422.svg' , 'university'),
        #('https://image.flaticon.com/icons/svg/1/1831.svg' , 'lion'),
        #('https://image.flaticon.com/icons/svg/90/90436.svg' , 'castle'),
        #('https://image.flaticon.com/icons/svg/14/14674.svg', 'shop'),
        #('https://image.flaticon.com/icons/svg/126/126054.svg' , 'bank'),
        #('https://image.flaticon.com/icons/svg/114/114505.svg' , 'hospital'),
        #('https://image.flaticon.com/icons/svg/83/83615.svg' , 'cafe'),
        #('https://image.flaticon.com/icons/svg/264/264085.svg' , 'restaurant'),
        #('https://image.flaticon.com/icons/svg/76/76272.svg' , 'hotel'),
        #('https://image.flaticon.com/icons/svg/8/8662.svg' , 'gas station'),
    #)
    #icon = models.CharField(max_length=200, choices=ICON_CHOICES, default='https://image.flaticon.com/icons/svg/89/89013.svg')
    def __str__(self):
        return self.title

class Carousel(models.Model):
  name = models.ForeignKey(Marker, blank=True, null=True)
  def __str__(self):
      return str(self.name)
