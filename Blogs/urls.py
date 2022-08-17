from Blogs.views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('all/', blogs, name="blogs"),
    path('new/', new_post, name="new_blog"),
    path('search', search, name="search"),
    path('search', search_results, name="search_results"),   
]