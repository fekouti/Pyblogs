from django.contrib import admin
from Accounts.models import *


# Register your models here.


@admin.register(User)
class Users_admin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']


@admin.register(User_profile)
class Users_Profile_admin(admin.ModelAdmin):
    list_display = ['user','name', 'lastname', 'user_bio','user_img']