from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import login, authenticate, logout

def blogs(request):
    posts = models.Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blogs.html', context)


def blog_detail(request, id):
    blog = models.Blog.objects.get(id=id)
    user = models.User.objects.get(id=id)
    social = models.SocialMedial.objects.filter(user=user)
    comments = models.Comment.objects.filter(blog=blog)
    context = {
        'user':user,
        'blog':blog,
        'socials':social,
        'comment_count':comments.count(),
        'comments':comments
    }
    return render(request, 'blog-detail.html', context)


def comment_create(request):
    message = request.POST['message']
    blog_id = request.POST['blog_id']
    models.Comment.objects.create(
        author=request.user,
        body=message,
        blog_id=blog_id
    )
    return redirect('blog_detail', blog_id)


def register_user(request):
    if request.method == 'POST':
        models.User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('index')