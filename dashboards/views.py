from django.shortcuts import redirect, render, get_object_or_404
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth.models import User
from dashboards.forms import CategoryForm, EditUserForm, PostForm, AddUserForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    posts_count=Blog.objects.all().count()
    context={
        'posts_count': posts_count
    }
    return render(request, 'dashboard/dashboard.html', context) 


def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if(request.method=='POST'):
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('categories')
    
    form=CategoryForm()
    context={ 'form': form }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category=Category.objects.get(id=pk)
    form=CategoryForm(instance=category)
    if(request.method=='POST'):
        form=CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('categories')
    context={ 'form': form , 'category': category}
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category=get_object_or_404(Category, id=pk)
    category.delete()
    return redirect('categories')
   

def posts(request):
    posts=Blog.objects.all()
    context={ 'posts': posts }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if(request.method=='POST'):
        form=PostForm(request.POST, request.FILES )
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            form.save()#to get primary key of the post
            post.slug=slugify(post.title)+'-'+str(post.id)
            form.save()#save the post again with the slug
        return redirect('posts')
    form=PostForm()
    context={
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)


def delete_post(request, pk):
    post=get_object_or_404(Blog, id=pk)
    post.delete()
    return redirect('posts')

def edit_post(request, pk):
    post = get_object_or_404(Blog, id=pk)
    author=post.author
    if request.user != author:
        return redirect('posts')

    if request.method == 'POST':
        # This is the only place the form is defined for a POST request.
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.slug = slugify(post.title) + '-' + str(post.id)
            form.save()
            return redirect('posts')
        # If invalid, the 'form' variable (with errors) still exists
        # and will be used in the context below.
    else:
        # This is the only place the form is defined for a GET request.
        form = PostForm(instance=post)

    # This context will now receive the correct 'form' object,
    # whether it's the initial GET form or the invalid POST form.
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html', context)



def users(request):
    users=User.objects.all()
    context={ 'users': users }  
    return render(request, 'dashboard/users.html',context)


def add_user(request):
    if(request.method=='POST'):
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form=AddUserForm()
    
    context={ 'form': form }
    return render(request, 'dashboard/add_user.html', context)


def delete_user(request, pk):
    user=get_object_or_404(User, id=pk)
    if not request.user==user:
        if user.is_superuser:
            if request.user.is_superuser:
                user.delete()
        else:
            user.delete()
    return redirect('users')


def edit_user(request, pk):
    user=get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)

    context = {
        'form': form,
        'user': user
    }
    return render(request, 'dashboard/edit_user.html', context)