from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})

def category_list(request):
    return render(request, 'category_list.html')