from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import store
from django.contrib.auth.models import auth
def fun(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        obj=store.objects.create(name=name,mobile=mobile,password=password)
        if password==confirm_password:
            obj.save()
            return  redirect('login')
        else:
            return  HttpResponse("invilid registration")
    else:
        return render(request,'store.html')
    


#----------LOGIN OPERATION--------------


def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        obj=store.objects.get(name=name,password=password)
        if(obj is not None):
            return redirect('home')
    else:
        return render(request,'store1.html')
    

#--------------WEBSITE MAIN PAGE AFTER LOGIN------------


def home(request):
    return render(request,'home.html')


#-------------LOGOUT OPERATION----------------


def logout(request):
    auth.logout(request)
    return redirect('login')
 