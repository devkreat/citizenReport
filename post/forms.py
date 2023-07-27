from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['address', 'decription', 'image']

        widgets = {
        'address' : forms.TextInput(attrs={'class ': 'form-control'}),
        'decription' : forms.Textarea(attrs={'class ': 'form-control'}),
        # 'image' : forms.ImageField(attrs={'class ': 'form-control'}),


        }
