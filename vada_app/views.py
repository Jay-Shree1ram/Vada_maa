from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import * 
from django.contrib.auth.decorators import login_required
from accounts.auth import *
from django.contrib.auth.models import User

# Create your views here.
@login_required
@admin_only
def dashboard(request):
    return render(request,"dashboard.html")

@login_required
@admin_only
def addcategory(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Category Added.")
            return redirect("/addcategory")

        else:
            messages.add_message(request,messages.ERROR,"Category not added.")
            context={
                'form':CategoryForm
            }
            return render(request,"addcategory.html",context)

    context={
        'form':CategoryForm
    }
    return render(request,"addcategory.html",context)

@login_required
@admin_only
def showcategory(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,"showcategory.html",context)

@login_required
@admin_only
def updatecategory(request,category_id):
    category=Category.objects.get(id=category_id)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Category update Succesfully.")
            return redirect("/showcategory")

        else:
            messages.add_message(request,messages.ERROR,"Category not updated.")
            context={
                'form':CategoryForm(instance=category)
            }
            return render(request,"updatecategory.html",context)
    context={
        'form':CategoryForm(instance=category)
    }
    return render(request,"updatecategory.html",context)

def deletecategory(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,"Category deleted succesfylly.")
    return redirect("/showcategory")
    
@login_required
@admin_only
def addvehicles(request):
    if request.method=="POST":
        form=VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Vehicles added succesfully.")
            return redirect("/addvehicles")

        else:
            messages.add_message(request,messages.ERROR,"Vehicles not added.")
            context={
                'form':VehicleForm

            }
            return render(request,"addvehicles.html",context)
            
        
    context={
        'form':VehicleForm

    }
    return render(request,"addvehicles.html",context)
@login_required
@admin_only
def showvehicles(request):
    vehicle=Vehicles.objects.all()
    context={
        'vehicle':vehicle
    }
    return render(request,"showvehicles.html",context)

@login_required
@admin_only
def updatevehicles(request,vehicle_id):
    vehicle=Vehicles.objects.get(id=vehicle_id)
    if request.method=="POST":
        form=VehicleForm(request.POST,request.FILES,instance=vehicle)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Vehicles update Succesfully.")
            return redirect("/showvehicles")

        else:
            messages.add_message(request,messages.ERROR,"Vehicles not updated.")
            context={
                'form':VehicleForm(instance=vehicle)
            }
            return render(request,"updatevehicles.html",context)
    context={
        'form':VehicleForm(instance=vehicle)
    }
    return render(request,"updatevehicles.html",context)

@login_required
@admin_only
def deletevehicles(request,vehicle_id):
    vehicle=Vehicles.objects.get(id=vehicle_id)
    vehicle.delete()
    messages.add_message(request,messages.SUCCESS,"Vehicles deleted succesfylly.")
    return redirect("/showvehicles")


# show contact us 
@login_required
@admin_only
def Contact_us(request):
    contact=Contact.objects.all()
    context={
        'contact':contact
    }
    return render(request,"contact.html",context)


