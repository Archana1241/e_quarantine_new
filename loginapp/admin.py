from django.contrib import admin
from.models import u_reg
from.models import p_reg
from.models import cnews
from.models import food
from.models import medicine
from.models import doctor
from.models import payment
from.models import FeedBackUser
# Register your models here.
admin.site.register(u_reg)
admin.site.register(p_reg)
admin.site.register(cnews)
admin.site.register(food)
admin.site.register(medicine)
admin.site.register(doctor)
admin.site.register(payment)
admin.site.register(FeedBackUser)