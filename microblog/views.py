from django.shortcuts import render, redirect
from .forms import CategoryForm, CustomUsersCreationForm, PostForm
from .models import Posts
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    posts = Posts.objects.select_related('user').all().order_by('-created_at')
    return render(request, 'home.html', { 'posts': posts })

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

class CustomSignUpView(CreateView):
    form_class = CustomUsersCreationForm
    template_name = 'register.html'
    success_url = '/login'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('microblog:home')

    # Esto es para asignar el usuario autenticado
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditPostView(LoginRequiredMixin, UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'edit_post.html'
    success_url = reverse_lazy('microblog:my_posts')
    # Esto es para validar que el post a editar corresponde al usuario autenticado
    def get_queryset(self):
        return Posts.objects.filter(user = self.request.user)

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('microblog:my_posts')

    # Esto es para validar que el post a eliminar corresponde al usuario autenticado
    def get_queryset(self):
        return Posts.objects.filter(user = self.request.user)
    
class MyPostsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'my_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Posts.objects.filter(user = self.request.user).select_related('user', 'category').order_by('-created_at')