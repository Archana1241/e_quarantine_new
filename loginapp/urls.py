from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    
    path('',views.mainhome,name='mainhome'),
    path('indexlogin1/',views.indexlogin1, name='indexlogin1'),
    path('reguser2/',views.reguser2, name='reguser1'),
    path('regpanchayat2/',views.regpanchayat2, name='regpanchayat2'),
    path('statistics/',views.statistics,name='statistics'),
    path('signupp/',views.signupp, name='signupp'),
    path('uhome/',views.uhome, name='uhome'),
    path('phome/<str:uname>',views.phome, name='phome'),
    path('indexadmin/',views.indexadmin, name='indexadmin'),
    path('logincheck/',views.logincheck, name='logincheck'),
    path('news/',views.news, name='news'),
    path('admvwfood2/',views.admvwfood2, name='admvwfood2'),
    path('admvwmedicine/',views.admvwmedicine, name='admvwmedicine'),
    path('admvwuser/',views.admvwuser, name='admvwuser'),
    path('admvwph/',views.admvwph, name='admvwph'),
    path('adminco1/',views.adminco1, name='adminco1'),
    path('logout/',views.logout, name='logout'),
    path('deleteph/<str:uname>',views.deleteph, name='deleteph'),
    path('deleteuser/<str:uname>',views.deleteuser, name='deleteuser'),
    path('addfood/',views.addfood, name='addfood'),
    path('addfood1/',views.addfood1, name='addfood1'),
    path('addmedicine/',views.addmedicine, name='addmedicine'),
    path('care/',views.care, name='care'),
    path('care1/',views.care1, name='care1'),
    path('foodorder/',views.foodorder, name='foodorder'),
    path('vwdoctor/',views.vwdoctor, name='vwdoctor'),
    path('medicineorder/',views.medicineorder, name='medicineorder'),
    path('userfoodorder/<int:id>',views.userfoodorder, name='userfoodorder'),
    path('usermedorder/<int:id>',views.usermedorder, name='usermedorder'),
    path('payment/<int:id>',views.payment, name='payment'),
    path('mpayment/<int:id>',views.mpayment, name='mpayment'),
    path('confirmuser/',views.confirmuser, name='confirmuser'),
    path('payment1/<int:id>',views.payment1, name='payment1'),
    path('payment2/<int:id>',views.payment2, name='payment2'),
    # path('pay/',views.pay, name='pay'),
    path('signupph/',views.signupph, name='signupph')
]
