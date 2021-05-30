from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class Contactinfo(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=12)
    fb_link = models.CharField(max_length=255, blank=True)
    insta_link = models.CharField(max_length=255, blank=True)
    tw_link = models.CharField(max_length=255, blank=True)
    yt_link = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

class Aboutinfo(models.Model):
    headline = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/about/")
    desc = RichTextField()

    def __str__(self):
        return self.headline
    