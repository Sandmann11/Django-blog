from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'title_tag', 'category', 'lead', 'text', 'image']

        widgets ={
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This will show as the browser tab title.'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'lead': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '500 characters max.'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'created_date': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }