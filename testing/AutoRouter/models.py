from django.db import models

# Create your models here.

class Router(models.Model):
    SSID = models.CharField(max_length=200)
    network_key = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)