from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction
from django.http import HttpResponse
from django.contrib.auth.models import User, auth



# Create your views here.



def save_transaction(request):
    # Your existing code for saving the transaction
     if request.method == 'POST':
        currency_one = request.POST.get('currency_one')
        amount_one = request.POST.get('amount_one')
        currency_two = request.POST.get('currency_two')
        amount_two = request.POST.get('amount_two')

        # Save the transaction in the database
        transaction = Transaction(
            currency_one=currency_one,
            amount_one=amount_one,
            currency_two=currency_two,
            amount_two=amount_two
        )
        transaction.save()
        print("data sent")

        return redirect('/index1')  # Redirect to a success page after saving the transaction


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
                return redirect('/registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/registration')
                     

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                print('user created')
                return redirect('/login')
           

        else:
            messages.info(request,'password not matching..')
            return redirect('/registration')
        
    else:    
        return render(request,'registration.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/index1")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')



    




