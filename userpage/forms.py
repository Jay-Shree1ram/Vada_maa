from .models import *
from django.forms import ModelForm,fields

class Book_nowForm(ModelForm):
    class Meta:
        model=Book_now
        fields=['Departure_date','Pickup_location1','Dropoff_location1','Return_date','Pickup_location2','Dropoff_location2']
        