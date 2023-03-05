from django.db import models
from django.contrib.auth.models import User
#create models
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField()
    digital= models.BooleanField(default=False, null=True, blank=False)
    # image

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    name = models.CharField(max_length=200, null=True)
    transaction_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
