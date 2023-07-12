from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User
from vada_app.models import *


# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)


class Book_now(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    Departure_date=models.DateField()
    Pickup_location1=models.CharField(max_length=100)
    Dropoff_location1=models.CharField(max_length=100)
    Return_date=models.DateField()
    Pickup_location2=models.CharField(max_length=100)
    Dropoff_location2=models.CharField(max_length=100)

    def __str__(self):
        return self.user,self.vehicle

