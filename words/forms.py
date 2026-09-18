from django import forms
from .models import Word
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
            'example': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'language': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']