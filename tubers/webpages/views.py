from django.shortcuts import render
from .models import Slider, Team
from contactinfo.models import Contactinfo
from youtubers.models import Youtuber

# Create your views here.
def home(request):
    sliders = Slider.objects.all()   #taken from model
    teams = Team.objects.all()
    contactinfos = Contactinfo.objects.all()
    featured_yt = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.all()

    data = {    #data is an object in which we passon and fetch all the informations. 
        'sliders': sliders,
        'teams': teams,
        'featured_yt': featured_yt,
        'all_youtubers': all_youtubers,
        'contactinfos': contactinfos,
        "abc":"pqr",
    }
    return render(request, 'webpages/home.html', data)  #passing the data in home template

def about(request):
    teams = Team.objects.all()

    data = {
        'teams': teams
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')
    
def contact(request):
    return render(request, 'webpages/contact.html')
