from django import forms
from .models import Categories, CustomUsers, Posts
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

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estas dos lineas son para para cargar contenido con listas desplegables
        self.fields['category'].queryset = Categories.objects.all()
        self.fields['category'].empty_label = "Seleccione una categoría"