from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import *

# Create your views here.
def user_register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"User added succesfully.")
            return redirect("/")

        else:
            messages.add_message(request,messages.ERROR,"User not added")
            context={
                'form':UserCreationForm
            }
            return render(request,"signup.html",context)
    context={
        'form':UserCreationForm
    }
    return render(request,"signup.html",context)


def signin(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,"Login Successful")
                return redirect("/dashboard")

            else:
                messages.add_message(request,messages.ERROR,"Login Failed.")
                context={
                    'form':LoginForm
                }
                return render(request,"signin.html",context)
    context={
        'form':LoginForm
    }
    return render(request,"signin.html",context)

def logout1(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,"Logout Successful.")
    return redirect("/")
