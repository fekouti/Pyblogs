from django.contrib import admin
from Blogs.models import *

# Register your models here.


@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'post_img','post_date','post_author','post_body']

