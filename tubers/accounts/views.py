from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # NOTE1: the above user object variable is available to all django templates bydefault but in the template folder.
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('loginuser')

    return render(request, 'accounts/loginuser.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():     #django has inbuilt model User
                message.error(request, 'Username exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email exixts!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()         #above create_user() is a inbuilt django function to create user.
                    messages.success(request, 'Account created successfully!')
                    return redirect('loginuser')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')


@login_required(login_url='loginuser')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
