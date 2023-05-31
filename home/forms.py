from django import forms
from.models import Profile, Post, Comments


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']

        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control bio'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'dateofbirth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields= ['image', 'caption']

        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'caption': forms.Textarea(attrs={'class': 'form-control'})
        }

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields= ['comment']

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }