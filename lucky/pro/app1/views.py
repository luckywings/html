from email.mime import base
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from flask import redirect
from app1 .models import *
from app1.form import *


# Create your views here.
def page1(request):
    return render(request, "page1.html",{'navbar':'page1'})


def base1(request):
    return render(request, "base1.html",{'navbar':'base1'})


def page3(request):
    return render(request, "page3.html",{'navbar':'page3'})


def base1(request):
    d=student.objects.all()
    return render(request,'base.html',{'s':d})

def form1(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if (form.is_valid()):
            form.save()
            return base(request)
    return render(request,'form1.html',{'form':form})

def form2(request):
    form=studentform()
    if(request.method =="POST"):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return base(request)
    return render(request,'form2.html')
       





def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already  exists!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')
                
      
    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(base)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(user_login)            
        