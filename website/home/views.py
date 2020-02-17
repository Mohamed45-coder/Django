from django.shortcuts import render,redirect
from .models import data
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

# The all-data function is used to upload the data from the admin side
def all_data(request):
    fields=data.objects.all()
    return render(request,'index.html', {'field':fields})

def first(request):
    return render(request,"first.html",)
def second(request):
    return render(request,"second.html")
def third(request):
   return render(request,"first.html")

# Register is used for signup 
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html',{'existing':"Existing username try differen name"})
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            
                user.save();

                print('user created')
                return redirect('/login') 
            
        else:
            return render(request,'signup.html',{'error':"password doesn't match"})


    return render(request,'signup.html')


# Used for login
def login(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        password=request.POST.get('password') 
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'invalid cerdentials')

    return render(request,"signup.html")
# used for logout
def logout(request):
    auth.logout(request)
    return redirect('/index')