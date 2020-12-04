from django.db import models

from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your models here.
class u_reg(models.Model):   
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mob=models.BigIntegerField() 
    hname= models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin = models.IntegerField()
    pname=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    status=models.IntegerField()

    def __str__(self):
        return self.uname

class p_reg(models.Model):
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100) 
    pname=models.CharField(max_length=100)
    cperson=models.CharField(max_length=100)
    mob=models.BigIntegerField() 
    uname=models.CharField(max_length=100)     
    status=models.IntegerField()

    def __str__(self):
        return self.cperson

class cnews(models.Model):
    ctotal = models.CharField(max_length=100)
    cactive = models.CharField(max_length=100)
    cured = models.CharField(max_length=100)
    death = models.CharField(max_length=100)

class food(models.Model):
    fitem = models.CharField(max_length=100)
    fquantity = models.IntegerField()
    fprice=models.IntegerField()

class medicine(models.Model):
    mname = models.CharField(max_length=100)
    mquantity = models.IntegerField()
    mprice=models.IntegerField()

class doctor(models.Model):
    dname = models.CharField(max_length=100)
    ddep = models.CharField(max_length=100)
    dmob=models.BigIntegerField()

    
    
       