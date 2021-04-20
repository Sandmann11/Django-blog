from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'title_tag', 'lead', 'text']

        widgets ={
            'author': forms.Select(attrs={'class': 'form-control',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'lead': forms.Textarea(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'image': forms.xxxxxxxxxx(attrs={'class': 'form-control'}),
            # 'created_date': forms.TextInput(attrs={'class': 'form-control'}),
        }