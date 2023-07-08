from .models import *
from django.forms import ModelForm,fields

# Models here
class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class VehicleForm(ModelForm):
    class Meta:
        model=Vehicles
        fields='__all__'

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        
