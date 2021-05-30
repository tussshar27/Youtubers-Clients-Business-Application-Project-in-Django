from django.db import models
# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=255) #blank=True can be used in parameter if we accept blank value. 
    subtext = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    #pillow library in django should be installed to use for image.
    photo = models.ImageField(upload_to='media/slider/%Y/%m/') # %Y = year, %m = month used to create folder based on it.
    created_date = models.DateTimeField(auto_now_add=True) 
    button_link = models.CharField(max_length=255, blank=True)

    def __str__(self):      #used to set name in db
        return self.headline