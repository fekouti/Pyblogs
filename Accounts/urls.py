
from django.contrib import admin
from django.urls import path
from Accounts.views import *
from Blogs.views import *

urlpatterns = [

    path('register/', create_user, name="new_user"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),

    path('<int:pk>/', profile.as_view(), name="profile"),
    path('edit/<int:pk>/', profile_edit.as_view(), name="profile_edit"),
    path('delete/<int:pk>/', UserDelete.as_view(), name="profile_delete"),


]