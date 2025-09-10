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
]