from django.shortcuts import render
from .models import Slider

# Create your views here.


def hello(request):
    data = Slider.objects.all()
    return render(request, 'index.html',{'data':data})


def about(request):
    return render(request, 'aboutus.html')


def tubers(request):
    return render(request, 'tubers.html')


def contactus(request):
    return render(request, 'contactus.html')


def signup(request):
    return render(request, 'register.html')


def user_login(request):
    return render(request, 'login.html')
