from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from Accounts.models import *
from Blogs.models import *



# ---- Order Blogs from timestamp ---- #

def blogHome(request):
    newposts = Post.objects.order_by('-timestamp')[0:5]
    featured = Post.objects.filter(is_featured = True)

    context = {'newposts': newposts, 'featured':featured}
    return render(request, 'index.html', context)
    



def about(request):
    return render(request, 'about.html', context={})



