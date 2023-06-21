from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.

def index1(request):
    return render(request,'index1.html')

def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('registration')
                     

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                print('user created')
           

        else:
            messages.info(request,'password not matching..')
            return redirect('registration')
        return redirect('/')
    else:    
        return render(request,'registration.html')

def login(request):
    return render(request,'login.html')            
