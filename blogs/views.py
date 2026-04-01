
from django.shortcuts import render,get_object_or_404,redirect
from .models import Category, Blog

# Create your views here.

def post_by_category(request, category_id):
   #fetch the blogs that belogs to the category with the given category_id and have status 'Published', ordered by updated_at
   blogs = Blog.objects.filter(category_id=category_id, status='Published').order_by('updated_at')

   #use get_object_or_404 to fetch the category with the given category_id, if not found return 404 error page
   category=get_object_or_404(Category, id=category_id)


  #use try except block when we want to do some custom action when the category with the given category_id is not found, in this case we will redirect to home page
#    try:
#       category = Category.objects.get(id=category_id)
#    except:
#       return redirect('home')
   context={
    'blogs': blogs,
    'category': category
   }
   return render(request, 'post_by_category.html', context)