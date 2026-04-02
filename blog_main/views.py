from django.contrib import auth
from django.urls import path
from django.shortcuts import redirect, render
from assignments.models import About
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from  blogs.models import Category,Blog 
def home(request):
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published').order_by('updated_at')
    try:
        about = About.objects.get()

    except:
        about=None
    context={   
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    form=RegistrationForm()
    context={
        'form': form
        }
    return render(request, 'register.html',context)


def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')  
            user=authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form=AuthenticationForm()
    context={
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')