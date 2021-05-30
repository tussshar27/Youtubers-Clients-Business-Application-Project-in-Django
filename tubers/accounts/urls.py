from django.urls import path
from . import views

urlpatterns = [
    path('loginuser', views.loginuser, name="loginuser"),
    path('logoutuser', views.logoutuser, name="logoutuser"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
]