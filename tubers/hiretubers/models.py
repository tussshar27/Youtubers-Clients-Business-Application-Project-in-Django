from django.db import models
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tuber_id = models.IntegerField()    #for the youtuber's page
    tuber_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)   #visiting user
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
    
class Contacttuber(models.Model):
    full_name = models.CharField(max_length=100)
    ph_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    comp_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    detail = models.TextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.full_name