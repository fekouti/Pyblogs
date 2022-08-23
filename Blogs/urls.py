from Blogs.views import *
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('all/', blogs, name="blogs"),

    path('new/', new_post, name="new_blog"),


    path('search', search, name="search"),
    path('search', search_results, name="search_results"),

    path('<int:pk>/', BlogDetail.as_view(), name='blogdetail'),

    path('delete/<int:pk>/', BlogDelete.as_view(), name='blogdelete'),

    path('edit/<int:pk>/', blog_edit.as_view(), name='blogedit'),

    path('tags/<str:name>/', tags_detail, name="tag_detail"),
]