from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blogs.models import Blog, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']  


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug','author',)



class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','is_staff','is_active', 'is_superuser','groups', 'user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','is_staff','is_active', 'is_superuser','groups', 'user_permissions')