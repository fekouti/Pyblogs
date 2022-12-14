from pyexpat import model
from turtle import title
from django.db import models
from django.urls import reverse
from django.conf import settings
from Accounts.models import *

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, null=True, unique=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=240)
    post_img = models.ImageField(upload_to='blog_image/', blank=True)
    post_date = models.DateField(auto_now_add=True)
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_body = models.TextField(blank=False)
    post_tags = models.ManyToManyField(to=Tag, blank=True, related_name='posts')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes', blank=True)

    def number_of_posts(self):
        return self.count()
    
    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if self.is_featured == True:
            Post.objects.filter(is_featured=True).update(is_featured=False)
        super().save(*args, **kwargs)


    @property
    def html_stripped(self):
       from django.utils.safestring import mark_safe
       return mark_safe(self.post_body)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
