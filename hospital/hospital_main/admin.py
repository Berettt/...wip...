from django.contrib import admin
from .models import *

# Register your models here.

#1 sposob
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass

#2 sposob
#admin.site.register(UserModel)
