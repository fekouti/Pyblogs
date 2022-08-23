from django.contrib import admin
from Blogs.models import *

# Register your models here.


@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'post_img','post_date','post_author','timestamp','is_featured']
    
@admin.register(Tag)
class Tag_admin(admin.ModelAdmin):
    list_display = ['name']
    
