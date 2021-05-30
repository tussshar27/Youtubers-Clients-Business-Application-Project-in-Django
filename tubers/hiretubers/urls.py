from django.urls import path
from . import views

urlpatterns = [
    path('hiretuber', views.hiretuber, name="hiretuber"),
    path('contacttuber', views.contacttuber, name="contacttuber"),
]