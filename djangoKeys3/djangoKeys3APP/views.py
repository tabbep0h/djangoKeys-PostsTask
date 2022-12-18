from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from .forms import *
from .models import *

def index(request):
    initialize()
    CreateForm = PostForm()
    if request.method == "POST":
        CreateForm = PostForm(request.POST)
        if CreateForm.is_valid():
            CreateForm.save()
            return redirect('/news')
    else:
        return render(request,"djangoKeys3APP/index.html",{"form":CreateForm})

def news(request):
    news = Post.objects.all()
    return render(request,"djangoKeys3APP/news.html",{"news":news})

def edit(request,id):
    try:
        post = Post.objects.get(id=id)
        editForm = PostForm
        if request.method == "POST":
            editForm = PostForm(request.POST,instance=post)
            if editForm.is_valid():
                editForm.save()
                return redirect('news')
        else:
            return render(request,'djangoKeys3APP/edit.html',{"post":editForm})
    except Post.DoesNotExist:
        return HttpResponse("<h2>Не найден</h2>")

def delete(request,id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect("news")
    except Post.DoesNotExist:
        return HttpResponse("<h2>Не найден</h2>")

def initialize():
    if Author.objects.all().count() == 0:
        Author.objects.create(name='Author 1')
        Author.objects.create(name='Author 2')
        Author.objects.create(name='Author 3')

    if Publisher.objects.all().count() == 0:
        Publisher.objects.create(name='Publisher 1')
        Publisher.objects.create(name='Publisher 2')
        Publisher.objects.create(name='Publisher 3')

    if Category.objects.all().count() == 0:
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')
        Category.objects.create(name='Category 3')