from django.shortcuts import render,redirect
from vada_app.models import *
from vada_app.forms import *
from django.contrib import messages
from accounts.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from userpage.models import *

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

def vehicles(request,vehicle_id):
    vehicle=Vehicles.objects.get(id=vehicle_id)
    context={
        'vehicle':vehicle
    }
    return render(request, "vehicles.html",context)

def Bookings(request,vehicle_id):
    user=request.user
    vehicle=Vehicles.objects.get(id=vehicle_id)
    check_presence=Booking.objects.filter(user=user,vehicle=vehicle)
    if(check_presence):
        messages.add_message(request,messages.ERROR,"Vehicles already in bookings.")
        return redirect("/mybooking")
    else:
        booking=Booking.objects.create(vehicle=vehicle,user=user)
        if booking:
            messages.add_message(request,messages.SUCCESS,"Vehicles added succesfuly.")
            return redirect("/mybooking")

        else:
            messages.add_message(request,messages.ERROR,"Items not added.")
            return redirect("")


def mybooking(request):
    user=request.user
    booking=Booking.objects.filter(user=user)
    context={
        'booking':booking
    }
    return render(request,"mybooking.html",context)

def Deletemybooking(request,booking_id):
    booking=Booking.objects.get(id=booking_id)
    booking.delete()
    messages.add_message(request,messages.SUCCESS,"Items delete Succesfully.")
    return redirect("/mybooking")


