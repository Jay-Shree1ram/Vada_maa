from django.db import models
from django.contrib.auth.models import User
from vada_app.models import *


# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)