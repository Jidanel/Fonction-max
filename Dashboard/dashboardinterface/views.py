from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def staff(request):
    return render(request,'staff.html')

def vehicules(request):
    return render(request,'vehicules.html') 

def vehiculearret(request):
    return render(request,'vehiculearret.html')

def vehiculeoccupe(request):
    return render(request,'vehiculeoccupe.html')

def profile(request):
    return render(request,'profile.html')