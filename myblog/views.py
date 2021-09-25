from django.shortcuts import render, redirect
from myblog.models import AboutModel, NavbarModel, Footer, PostModel, Settings, PostModel,PostImageModel
from .forms import PostContactForm, PostCreateForm
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model, authenticate, login 
from django.contrib.auth.decorators import login_required

User = get_user_model

@login_required(login_url='login_page')

def home_view(request):
    context = {}
    posts_queryset = PostModel.objects.all()
    context['posts_queryset']= posts_queryset
    return render (request , 'index.html', context)

def post_detail_view(request, post_id):
    context = {}
    post_detail_queryset = PostModel.objects.filter(id=post_id).first()
    post_detail_images = PostImageModel.objects.filter(post_id=post_id)
    context['post_detail_queryset'] = post_detail_queryset
    context['post_detail_images'] = post_detail_images
    return render(request, 'post_detail.html', context)

def about_detail_view(request):
    context = {}
    text_queryset = AboutModel.objects.filter().first()
    context['text_queryset'] = text_queryset
    return render(request,'about.html', context)

def post_contact_view(request):
    context = {}
    form = PostContactForm()
    if request.method == 'POST':
        form = PostContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        else:
            context['form'] = form
            return render(request, 'contact.html',context)

    context['form'] = form
    return render(request, 'contact.html', context)

def post_create_view(request):
    context = {}
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.save()
            return redirect('home_page')
        else:
            context['form'] = form
            return render(request, 'post_create.html',context)

    context['form'] = form
    return render(request, 'post_create.html',context) 

def post_view(request):
    context = {}
    posts_queryset = PostModel.objects.all()
    context['posts_queryset']= posts_queryset
    return render(request, 'posts.html', context) 

def register_view(request):
    context = {}
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            context['form'] = form
            return render(request, 'register.html', context)
    
    context['form'] = form
    return render(request, 'register.html', context)

def login_view(request):
    context = {}
    username = request.POST.get('username')
    raw_password = request.POST.get('password')
    user = authenticate(username=username, password=raw_password)
    if user:
        login(request, user)
        return redirect('home_page')
    else:
        print("ERRRORRRRRRRR")
        context['error message'] = 'ERROR'
        return render(request, 'login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('login_page')