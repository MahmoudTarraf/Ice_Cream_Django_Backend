from django.db import models

class Order(models.Model):
    email = models.CharField(max_length=50)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    delivered = models.CharField(max_length=50)
    operationNumber = models.CharField(max_length=50,unique=True)
    phonenumber = models.CharField(max_length=20,default='')
    location = models.CharField(max_length=100,default='')
    username = models.CharField(max_length=150,default='')

    def __str__(self):
        return f"Order {self.id}"