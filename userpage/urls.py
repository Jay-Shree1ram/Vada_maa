from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home),
    path("vehicle/<int:vehicle_id>",vehicles),
    path("booking/<int:vehicle_id>",Bookings),
    path('mybooking/',mybooking),
    path('deletemybooking/<int:booking_id>',Deletemybooking),
    path('booknow/<int:vehicle_id>/<int:booking_id>',Booknow_form)
    
    
]