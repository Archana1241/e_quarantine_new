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
    path('phome/',views.phome, name='phome'),
    path('indexadmin/',views.indexadmin, name='indexadmin'),
    path('logincheck/',views.logincheck, name='logincheck'),
    path('news/',views.news, name='news'),
    path('admvwfood2/',views.admvwfood2, name='admvwfood2'),
    path('admvwmedicine/',views.admvwmedicine, name='admvwmedicine'),
    path('admvwuser/',views.admvwuser, name='admvwuser'),
    path('admvwph/',views.admvwph, name='admvwph'),
    path('adminco1/',views.adminco1, name='adminco1'),
    path('updatedoctor/<int:id>',views.updatedoctor, name='updatedoctor'),
    path('logout/',views.logout, name='logout'),
    path('deleteph/<str:uname>',views.deleteph, name='deleteph'),
    path('deleteuser/<str:uname>',views.deleteuser, name='deleteuser'),
    path('addfood/',views.addfood, name='addfood'),
    path('addfood1/',views.addfood1, name='addfood1'),
    path('addmedicine/',views.addmedicine, name='addmedicine'),
    path('care/',views.care, name='care'),
    path('care1/',views.care1, name='care1'),
    path('care2/',views.care2, name='care2'),
    
    path('foodorder/',views.foodorder, name='foodorder'),
    path('vwdoctor/',views.vwdoctor, name='vwdoctor'),
    path('phvwdoctor/',views.phvwdoctor,name='phvwdoctor'),
    path('deletedoctor/<int:id>',views.deletedoctor,name='deletedoctor'),
    path('editdoctor/<int:id>',views.editdoctor,name='editdoctor'),
    path('usetpwd/',views.usetpwd, name='usetpwd'),
    path('phpwd/',views.phpwd, name='phpwd'),
    
    path('deletefood/<str:uname>/<str:pname>',views.deletefood, name='deletefood'),
    path('deletemedicine/<str:uname>/<str:pname>',views.deletemedicine, name='deletemedicine'),
    path('deletefood1/<int:id>',views.deletefood1, name='deletefood1'),
    path('deletemedicine1/<int:id>',views.deletemedicine1, name='deletemedicine1'),
    path('medicineorder/',views.medicineorder, name='medicineorder'),
    path('userfoodorder/<int:id>',views.userfoodorder, name='userfoodorder'),
    path('usermedorder/<int:id>',views.usermedorder, name='usermedorder'),
    path('payment/<int:id>/<str:uname>',views.payment, name='payment'),
    path('mpayment/<int:id>/<str:uname>',views.mpayment, name='mpayment'),
    path('confirmuser/<str:pname>',views.confirmuser, name='confirmuser'),
    path('payment1/<int:id>/<str:uname>',views.payment1, name='payment1'),
    path('payment2/<int:id>/<str:uname>',views.payment2, name='payment2'),
    path('phnotification/<str:pname>',views.phnotification, name='phnotification'),
    path('userfeedback/',views.userfeedback, name='userfeedback'),
    path('newfun/<int:id>',views.newfun, name='newfun'),
    
    path('complaintsave/<int:id>/<str:spname>',views.complaintsave, name='complaintsave'),
    # path('complaintvw/',views.complaintvw, name='complaintvw'),
    path('comview/<str:spname>',views.comview, name='comview'),
     path('comreply/<str:uname>', views.comreply, name='comreply'),
    path('signupph/',views.signupph, name='signupph')
     
    ]

