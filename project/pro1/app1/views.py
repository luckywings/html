from django.shortcuts import render
from app1.models import *

from app1.form import *
# Create your views here.
def home(request):
    return render(request,'base.html')


def upload(request):
    form=bookform()
    if(request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home (request)
    return render (request,'add.html',{'form':form})

def booklist(request):
    b=Book.objects.all()
    return render(request,'list.html',{'b':b})

# def add(request):
#     return render(request,'add.html')

# def list(request):
#     return render(request,'list.html')
