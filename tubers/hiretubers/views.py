from django.shortcuts import redirect, render
from .models import Hiretuber, Contacttuber
from django.contrib import messages

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     tuber_id = models.IntegerField()    #for the youtuber's page
#     tuber_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     message = models.TextField(blank=true)
#     phone = models.CharField(max_length=100)
#     user_id = models.IntegerField(blank=True)   #visiting user

# Create your views here.
def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']     #overriding 'id' field from frontend
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']

        # TODOs: do all the sanitization work 
        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, email=email, city=city, state=state, message=message, phone=phone, user_id=user_id)
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')


    # full_name = models.CharField(max_length=100)
    # ph_number = models.CharField(max_length=12)
    # email = models.EmailField(max_length=100)
    # comp_name = models.CharField(max_length=200)
    # subject = models.CharField(max_length=200)
    # detail = models.TextField()

def contacttuber(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        ph_number = request.POST['ph_number']
        email = request.POST['email']
        comp_name = request.POST['comp_name']
        subject = request.POST['subject']
        detail = request.POST['detail']

        contacttuber = Contacttuber(full_name=full_name, ph_number=ph_number, email=email, comp_name=comp_name, subject=subject, detail=detail)
        contacttuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('contact')

