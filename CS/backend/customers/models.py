from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key= True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    shipping_address = models.TextField(max_length=30, blank=True, null=True)
    loyalty_points = models.CharField(max_length=30, blank=True, null=True)
    payment = models.CharField(max_length= 120)
    cc_num = models.CharField(max_length= 120)
    exp = models.CharField(max_length= 120)
    cvv = models.CharField(max_length= 120)