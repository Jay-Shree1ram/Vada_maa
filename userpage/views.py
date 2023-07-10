from django.shortcuts import render,redirect
from vada_app.models import *
from vada_app.forms import *
from django.contrib import messages
from accounts.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    vehicle=Vehicles.objects.all()
    context={
        'vehicle':vehicle
    }
    if request.method=='POST':
       
        form=ContactForm(request.POST)
        form.save()
        messages.add_message(request,messages.SUCCESS,"Thanks for contacting us.")
        

    return render(request,"home.html",context)


