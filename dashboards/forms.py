from django import forms

from blogs.models import Blog, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']  


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug','author',)