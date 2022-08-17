from pyexpat import model
from turtle import title
from django.db import models
from Accounts.models import *

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=240)
    post_img = models.ImageField(upload_to='blog_image/', blank=True)
    post_date = models.DateField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_body = models.CharField(max_length=140000)
    post_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
