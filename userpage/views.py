from django.shortcuts import render,redirect
from vada_app.models import *
from vada_app.forms import *
from django.contrib import messages
from accounts.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from userpage.models import *
from .forms import *

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

@login_required
@user_only

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

@login_required
@user_only
def mybooking(request):
    user=request.user
    booking=Booking.objects.filter(user=user)
    context={
        'booking':booking
    }
    return render(request,"mybooking.html",context)

@login_required
@user_only
def Deletemybooking(request,booking_id):
    booking=Booking.objects.get(id=booking_id)
    booking.delete()
    messages.add_message(request,messages.SUCCESS,"Items delete Succesfully.")
    return redirect("/mybooking")

@login_required
@user_only
def Booknow_form(request,vehicle_id,booking_id):
    user=request.user
    vehicle=Vehicles.objects.get(id=vehicle_id)
    booking=Booking.objects.get(id=booking_id)
    if request.method=="POST":
        form=Book_nowForm(request.POST)
        if form.is_valid():
            Departure_date=request.POST.get('Departure_date')
            Pickup_location1=request.POST.get('Pickup_location1')
            Dropoff_location1=request.POST.get('Dropoff_location1')
            Return_date=request.POST.get('Return_date')
            Pickup_location2=request.POST.get('Pickup_location2')
            Dropoff_location2=request.POST.get('Dropoff_location2')


            book_now=Book_now.objects.create(
                vehicle=vehicle,
                user=user,
                Departure_date=Departure_date,
                Pickup_location1=Pickup_location1,
                Dropoff_location1=Dropoff_location1,
                Return_date=Return_date,
                Pickup_location2=Pickup_location2,
                Dropoff_location2=Dropoff_location2

            )
            booking=Booking.objects.get(id=booking_id)
            booking.delete()
            messages.add_message(request,messages.SUCCESS,"Order successful.")
            return redirect("/mybooking")




    context={
        'form':Book_nowForm
    }
    return render(request,"booknow.html",context)



