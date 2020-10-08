from django import forms
from .models import *

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'image', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': 'user.id',}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-integer', }),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ('name', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }