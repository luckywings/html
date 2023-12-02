from django.shortcuts import render
from django.http import HttpResponse
from app1.models import*
from app1.form import *
# Create your views here.
def home(request):
    return render(request,'home.html')
def home(request):
    d={'name':'sam','age':20}
    return render(request,'home.html',d)

def index(request):
    return HttpResponse('hello welcome to this page')

def intro(request):
    return HttpResponse('hyy!!!')

def home(request):
    d=student.objects.all()    
    return render(request,'home.html',{'s',d})

def form1(request):
    form=studentform()
    if(request.method =="POST"):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'form1.html',{'form':form})

def form2(request):
   
    if(request.method =="POST"):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'form2.html')
