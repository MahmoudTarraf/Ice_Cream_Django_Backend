from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=50,unique=True)
    phonenumber = models.CharField(max_length=20,blank=True)
    location = models.CharField(max_length=100,blank=True)
    points = models.CharField(max_length=100,blank=True)
    total_purchases = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.username