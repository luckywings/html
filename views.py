from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")

def product_list(request):
    return render(request, "product_list.html")