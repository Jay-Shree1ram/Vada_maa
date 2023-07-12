from django.urls import path,include
from .views import *


urlpatterns = [

    path("dashboard/",dashboard),
    path("addcategory/",addcategory),
    path("addvehicles",addvehicles),
    path("showcategory/",showcategory),
    path("showvehicles/",showvehicles),
    path("updatecategory/<int:category_id>",updatecategory),
    path("updatevehicles/<int:vehicle_id>",updatevehicles),
    path("deletecategory/<int:category_id>",deletecategory),
    path("deletevehicles/<int:vehicle_id>",deletevehicles),
    path("contact_us/",Contact_us),
    path('users/',users),
    path('totalbooking/',Total_booking),

]