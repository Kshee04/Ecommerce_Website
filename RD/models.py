from django.db import models
from django.contrib.auth.models import User
#create models
class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True )
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)

    def __str__(self):__