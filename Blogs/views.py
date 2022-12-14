from multiprocessing import context
from tkinter import FLAT
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.views.generic import *
from django.contrib.auth.decorators import login_required

from Blogs.models import *


# Create your views here.

# ---- List all Blogs ---- #

def blogs(request):
     blogs = Post.objects.all().order_by('-timestamp')
     tags = Tag.objects.all()
    
     context = {"blogs":blogs, "tags":tags}

     return render(request,"blogs.html",context = context)


# ---- Create New Blog ---- #


@login_required
def new_post(request):

    if request.method == 'POST':

        title= request.POST['title']

        subtitle= request.POST['subtitle']

        post_body= request.POST['post_body']

        post_img= request.POST.get('post_img')
        post_img= request.FILES.get('post_img')

        post_author = request.user
       
        new_post = Post(title=title, subtitle=subtitle, post_body=post_body, post_img=post_img, post_author=post_author)

        
        new_post.save()

        tags = request.POST.getlist('post_tags')

        new_post_tags = []
        
        for name in tags:
            try:
                tag = Tag.objects.get(name=name)
            finally:
                new_post_tags.append(tag)

        if tags is not None:

            new_post.post_tags.add(*new_post_tags)

        

        return redirect('../../../blogs/all/')

    tags = Tag.objects.all()
    context = {"tags":tags}


    return render(request, 'new_post.html', context=context)


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

class blog_edit(UpdateView):
    model = Post
    success_url = '../../../blogs/all/'
    fields = ['title', 'subtitle', 'post_img', 'post_body']
    template_name = 'edit_post.html'

# ---- Delete Blogs ---- #

class BlogDelete(DeleteView):
    model = Post
    template_name = 'post.html'
    success_url = '../../../blogs/all/'


# ---- Read Blogs ---- #


class BlogDetail(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


# ---- Tag Posts ---- #

def tags_detail(request, name):
    tags = Tag.objects.get(name__iexact=name)

    blogs = Post.objects.filter(post_tags=tags)
    
    context = {"blogs":blogs, "tags":tags}
   
    return render(request, 'tag_results.html', context=context)

# ---- Posts Likes ---- #

def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('../../blogs/'+ str(pk))