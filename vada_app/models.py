from django.db import models
from tkinter import CASCADE 

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.category_name

class Vehicles(models.Model):
    vehicles_type=models.CharField(max_length=50)
    vehicles_rate=models.FloatField()
    vehicles_image=models.FileField(upload_to='static/uploads',null=True)
    vehicles_no=models.CharField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicles_type

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name