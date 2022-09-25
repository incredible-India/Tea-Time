from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True,null=False)
    password = models.CharField(max_length=250)
    upi = models.CharField(max_length=250)