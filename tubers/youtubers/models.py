from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Youtuber(models.Model):

    crew_choice = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )
    
    camera_choice = (
        ('sony', 'sony'),
        ('nikon', 'nikon'),
        ('canon', 'canon'),
        ('red', 'red'),
        ('fujifilm', 'fujifilm'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    )

    category_choice = (
        ('coding', 'coding'),
        ('tech', 'tech'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('filming', 'filming'),
        ('gaming', 'gaming'),
        ('cooking', 'cooking'),
    )
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/%d/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choice, max_length=255)
    camera_type = models.CharField(choices=camera_choice, max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices=category_choice, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
                #Note: default=datetime.now is similar to auto_now_add=True just that we have to import datetime in it.
                #in datetime we can edit date & time manually in admin page where as in auto_now_add the date and time are stored automatically.