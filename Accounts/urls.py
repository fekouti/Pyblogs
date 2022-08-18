from Accounts.views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('register/', create_user, name="new_user"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
    path('<str:username>/', profile, name="profile"),
]