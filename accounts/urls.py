from django.urls import path,include
from .views import *

urlpatterns = [
    path('signup/',user_register),
    # path('login/',signin),
    path('accounts/login/',signin),
    path('logout/',logout1),
]