from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt


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
    path('usetpwd/',views.usetpwd, name='usetpwd'),
    path('phpwd/',views.phpwd, name='phpwd'),
    # path('admpw/',views.admpw, name='admpw'),
    # path('usetpwd1/',views.usetpwd1, name='usetpwd1'),
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
    # path('pay/',views.pay, name='pay'),
    path('signupph/',views.signupph, name='signupph'),
    path('fpass/',views.forgotpass, name='fpass'),
    path('cpass/',views.otp_pass, name='cpass'),
    path('userfeedback/', views.userfeedback, name="userfeedback"),
    path('user_feedback_save/', views.user_feedback_save, name="user_feedback_save"),
    path('user_feedback_message/', views.user_feedback_message,name="user_feedback_message"),
    path('user_feedback_message_replied/', views.user_feedback_message_replied,name="user_feedback_message_replied"),
]
