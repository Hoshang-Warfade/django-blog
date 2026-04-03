from django.shortcuts import redirect, render, get_object_or_404
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm

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
   