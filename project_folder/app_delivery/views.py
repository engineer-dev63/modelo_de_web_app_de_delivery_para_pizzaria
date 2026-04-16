from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'app_delivery/main/home.html' )

def menu(request):
    return render(request, 'app_delivery/main/menu.html')

def login(request):
    return render(request, 'app_deelivery/main/login.html')

def aboutus(request):
    return render(request, 'app_delivery/main/aboutus.html')