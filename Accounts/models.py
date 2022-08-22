import email
from typing_extensions import Required
from django.conf import settings
from django.db import models

# Create your models here.



class User(models.Model):


    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE, )
    email = models.EmailField(max_length=40, unique=True, blank=True)
    password = models.CharField(max_length=12, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    user_bio = models.TextField()
    user_img = models.ImageField(default='default.jpg', upload_to='profile_image/', blank=True)

    def __str__(self):
        return self.user.username + ' - profile'




