from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Blogs.models import *
from django.http import HttpResponse

# Create your views here.

# ---- List all Blogs ---- #

def blogs(request):
     blogs=Post.objects.all()
     context = {"blogs":blogs}
     return render(request,"blogs.html",context = context)


# ---- Create New Blog ---- #


# def new_blog(request):
#     return render(request, 'new_post.html', context={})


@login_required
def new_post(request):
    
    if request.method == 'POST':
        

        title= request.POST['title']

        subtitle= request.POST['subtitle']

        post_body= request.POST['post_body']

        post_img= request.POST['post_img']


       
        new_post = Post(title=title, subtitle=subtitle, post_body=post_body, post_img=post_img)

        new_post.save()

        return redirect('/')


    return render(request, 'new_post.html', context={})


# ---- Search Among Blogs ---- #

def search_results(request):
    return render(request, "search.html",context={})


def search(request):
    if request.method == 'GET':

        if request.GET['Search']:

            post = request.GET['Search']
            posts = Post.objects.filter(title__icontains=post)

            return render(request, "search.html", {"posts":posts , "post":post})

        else:

            response = "No se encontraron resultados :("

    return HttpResponse(response)



# ---- Edit Blogs ---- #




# ---- Delete Blogs ---- #



# ---- Read Blogs ---- #