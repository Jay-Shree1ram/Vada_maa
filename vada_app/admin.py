from django.contrib import admin
from .models import *
from userpage.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Vehicles)
admin.site.register(Contact)
admin.site.register(Book_now)