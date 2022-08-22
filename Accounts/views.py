from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import *
from django.contrib.auth import login, logout, authenticate

from Accounts.models import *
from Blogs.models import *
from .forms import *



# Create your views here.



# ---- Register ---- #

def create_user(request):
    
    if request.method == 'POST':
        

        username= request.POST['username']

        email= request.POST['email']

        password= request.POST['password']

        name= request.POST['name']

        lastname= request.POST['lastname']

        user_bio= request.POST['user_bio']

        user_img= request.POST.get('user_img')
        user_img= request.FILES.get('user_img')

       
        

       
        new_user = User.objects.create_user(username=username, email=email, password=password)
        
        User.set_password(User, password)

        new_user.save()

        new_profile = Profile(user=new_user, name=name, lastname=lastname, user_bio=user_bio, user_img=user_img)
        

        new_profile.save()

        return redirect('../login/')


    return render(request, 'register.html', context={})




# ---- Login & Logout ---- #


def login_request(request):

    
    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']


        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
        
            return redirect('/')         

        else:
            return redirect('login/')


    return render(request, 'login.html', context={})



def logout_request(request):

    logout(request)

    return redirect("/")




# ---- Profiles ---- #


# ---- Read Profiles ---- #


class profile(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    # def blogs(user):
    #     blogs = Post.objects.all().order_by('-timestamp')
    #     context = {
    #         'blogs':blogs
    #     }
    #     return render(context) 

    def get_context_data(self, **kwargs):
        context = super(profile, self).get_context_data(**kwargs)
        context['blogs'] = Post.objects.all().order_by('-timestamp')
        return context
    

# ---- Edit Profiles ---- #

class profile_edit(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['user_img','user_bio']
    template_name = 'edit_profile.html'


# ---- Delete Profiles ---- #

class UserDelete(DeleteView):
    model = User
    template_name = 'profile.html'
    success_url = '/'

