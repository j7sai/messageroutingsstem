from django.db import models

# Create your models here.

class Gateway(models.Model):
    name = models.CharField(max_length=200,unique=True)

class IPaddress(models.Model):
    gatewayId =models.ForeignKey(Gateway,on_delete=models.CASCADE,related_name="ipaddress")
    address = models.CharField(max_length=200)

class Router(models.Model):
    gateway =models.OneToOneField(Gateway,on_delete=models.CASCADE,related_name="gateway",unique=True)
    prefix = models.CharField(max_length=200)