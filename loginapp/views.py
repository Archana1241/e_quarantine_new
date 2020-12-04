
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import View
from django.template.loader import get_template
from . models import u_reg
from . models import p_reg
from . models import cnews
from . models import food
from . models import medicine
from . models import doctor
from django.core.files.storage import FileSystemStorage
# Create your views here.

def mainhome(request):
    pf = cnews.objects.filter()
    return render(request, "index1.html",{'pf':pf})
def indexlogin1(request):
    return render(request, "indexlogin1.html")    
def reguser2(request):
    return render(request, "reguser2.html")  
def regpanchayat2(request):
    return render(request, "regpanchayat2.html") 
def addfood(request):
    if request.method == 'POST':
        fitem = request.POST['fitem']
        fquantity= request.POST['fquantity']
        fprice = request.POST['fprice']  
        fod=food(fitem=fitem,fquantity=fquantity,fprice=fprice)
        fod.save()
    return render(request, "addfood.html") 
def addmedicine(request):
    if request.method == 'POST':
        mname = request.POST['mname']
        mquantity= request.POST['mquantity']
        mprice = request.POST['mprice']  
        med=medicine(mname=mname,mquantity=mquantity,mprice=mprice)
        med.save()
    return render(request, "addmedicine.html") 
def care(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        ddep= request.POST['ddep']
        dmob = request.POST['dmob']  
        dep=doctor(dname=dname,ddep=ddep,dmob=dmob)
        dep.save()
    return render(request, "care.html") 
def phome(request):
    
    # pff=cnews.objects.filter()
    # s=user.username
    # j=p_reg.objects.filter(uname=s)
    return render(request, "phome.html")    
def uhome(request):
    return render(request, "uhome.html")   
def indexadmin(request):
    return render(request, "indexadmin.html")  
def news(request):
    pp = cnews.objects.filter()
    return render(request, "news.html" ,{'pp':pp})  
def logout(request):
    return render(request,'index1.html')     
def adminco1(request):
     if request.method == 'POST':
        ctotal1 = request.POST['ctotal']
        cactive1 = request.POST['cactive']
        cured1 = request.POST['cured']  
        death1 = request.POST['death']
        # cov=cnews(ctotal=ctotal,cactive=cactive,cured=cured,death=death)
        # cov.save()
        # return render(request,'news.html')

       
        pp=cnews.objects.get()
        pp.ctotal=ctotal1
        pp.save()
        pp.cactive=cactive1
        pp.save()
        pp.cured=cured1
        pp.save()
        pp.death=death1
        pp.save()
        
        return redirect( '/news')
     else:
        return render(request,'news.html')       
def admvwfood2(request):
    return render(request, "admvwfood2.html") 
def admvwmedicine(request):
    return render(request, "admvwmedicine.html")           
def admvwuser(request):
    # i = u_reg.objects.filter(status="1")
    s = u_reg.objects.filter()
    return render(request, "admvwuser.html" ,{'s':s})   
def admvwph(request):
    i = p_reg.objects.filter(status="1")
    return render(request, "admvwph.html",{'i':i})
def deleteph(request,uname):
    d=p_reg.objects.get(uname=uname)
    d.status = 0
    d.save()
    u=User.objects.get(username=uname)
    u.is_active = False
    u.save()
    return redirect('admvwph')       
def signupp(request):
   if request.method == 'POST':
        fname = request.POST['fname']
        lname=request.POST['lname']
        mob=request.POST['mob']
        hname = request.POST['hname']
        place = request.POST['place']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        pname = request.POST['pname']
        uname = request.POST['uname']
        pwd= request.POST['pwd']
        pwd1 = request.POST['pwd1']
        if(pwd == pwd1):
            if User.objects.filter(username=uname).exists():                                                                 
                messages.info(request,'Username already exist')
                return render(request, 'reguser2.html') 
            user = User.objects.create_user(username=uname, password=pwd, email=uname, first_name=fname, last_name=lname)
            user.save()
            usr=u_reg(fname=fname,lname=lname,mob=mob,hname=hname,place=place,district=district,state=state,pin=pin,pname=pname,uname=uname,status='1')
            usr.save()
            return render(request, 'indexlogin1.html') 
        else: 
            messages.info(request,'Password Missmatch')
            return render(request, 'reguser2.html')
         
   else:
        return render(request, 'reguser2.html') 

def signupph(request):
   if request.method == 'POST':
        state = request.POST['state']
        district=request.POST['district']
        pname = request.POST['pname']
        cperson = request.POST['cperson']
        mob=request.POST['mob']
        uname=request.POST['uname']
        pwdd= request.POST['pwdd']
        pwdd1 = request.POST['pwdd1']
        if(pwdd == pwdd1):
            if User.objects.filter(username=uname).exists():                                                                 
                messages.info(request,'Username already exist')
                return render(request, 'regpanchayat2.html') 
            user = User.objects.create_user(username=uname, password=pwdd, email=uname, first_name=cperson, last_name="ph")
            user.save()    
            phr=p_reg(state=state,district=district,pname=pname,cperson=cperson,mob=mob,uname=uname,status='1')
            phr.save()
            
            return render(request, 'indexlogin1.html') 
        else: 
            messages.info(request,'Password Missmatch')
            return render(request, 'regpanchayat2.html')
         
   else:
        return render(request, 'regpanchayat2.html')          


def logincheck(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        if u_reg.objects.filter(uname=username).exists():
            usr=u_reg.objects.get(uname=username)
            if usr.status == 1:
                  user = auth.authenticate(username=username, password=password)
                  if user is not None:
                     auth.login(request, user) 
                     if User.objects.filter(last_name="ph",username=username).exists():
                        return render(request, 'phome.html')   
                     else:    
                         return render(request, 'uhome.html') 
                  else:
                      
                      messages.info(request, 'invalid username/password')
                      return render(request, 'indexlogin1.html')
            else:
                messages.info(request,'Your account is deactivated')    
                return render(request, 'indexlogin1.html')
        elif p_reg.objects.filter(uname=username).exists():
             phr=p_reg.objects.get(uname=username)
             if phr.status == 1:
                 user = auth.authenticate(username=username, password=password)
                 if user is not None:
                     auth.login(request, user) 
                     if User.objects.filter(last_name="ph",username=username).exists():
                        return render(request, 'phome.html')
                     else:
                         return render(request,'uhome.html')
                 else:
                     messages.info(request, 'invalid username/password')
                     return render(request, 'indexlogin1.html')
             else:
                 messages.info(request,'Your account is deactivated')    
                 return render(request, 'indexlogin1.html')
        else: 
             user = auth.authenticate(username=username, password=password)
             if user is not None:
                auth.login(request, user)
                return redirect('indexadmin')
             else:
                 messages.info(request, 'invalid username/password')
                 return render(request, 'indexlogin1.html')
    else:             
        return render(request, 'indexlogin1.html')
                        
