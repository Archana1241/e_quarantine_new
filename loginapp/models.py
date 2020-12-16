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
    f_status =models.TextField()
    m_status =models.TextField()
    f_id=models.IntegerField()
    m_id=models.IntegerField()


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
    india=models.CharField(max_length=100)
    i_active = models.CharField(max_length=100)
    i_recoverd=models.CharField(max_length=100)
    i_death=models.CharField(max_length=100)
    world=models.CharField(max_length=100)
    w_active = models.CharField(max_length=100)
    w_recoverd=models.CharField(max_length=100)
    w_death=models.CharField(max_length=100)

class food(models.Model):
    uname=models.CharField(max_length=100)
    u_name=models.CharField(max_length=100)
    pname =models.CharField(max_length=100)
    fitem = models.CharField(max_length=100)
    
    fprice=models.IntegerField()
    status =models.TextField()


class medicine(models.Model):
    uname=models.CharField(max_length=100)
    u_name=models.CharField(max_length=100)
    pname =models.CharField(max_length=100)
    
    mname = models.CharField(max_length=100)
    
    mprice=models.IntegerField()
    status =models.TextField()
    quantity=models.IntegerField()

class doctor(models.Model):
    pname =models.CharField(max_length=100)
    dname = models.CharField(max_length=100)
    ddep = models.CharField(max_length=100)
    dmob=models.BigIntegerField()
    img=models.ImageField(upload_to='media/pics',blank=True)

class payment(models.Model):  
    pamt=models.IntegerField()
    cname=models.CharField(max_length=100)
    cno=models.IntegerField()
    expno=models.CharField(max_length=100)
    cvv=models.IntegerField()
    
class complaints(models.Model):
    uname=models.CharField(max_length=100)
    spname =models.CharField(max_length=100)
    details = models.TextField() 
    replay = models.TextField()
    status =models.TextField()
    r_status = models.TextField()  