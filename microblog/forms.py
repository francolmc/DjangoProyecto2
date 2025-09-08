from django import forms
from .models import Categories, CustomUsers
from django.contrib.auth.forms import UserCreationForm

class CustomUsersCreationForm(UserCreationForm):
    class Meta:
        model = CustomUsers
        fields = ('username', 'email', 'first_name',
                  'last_name', 'personal_url')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }