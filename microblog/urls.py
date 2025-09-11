#imports
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'microblog'

#configuracion
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.CustomSignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('my_posts/', views.MyPostsView.as_view(), name='my_posts'),
    path('edit_post/<int:pk>/', views.EditPostView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
]