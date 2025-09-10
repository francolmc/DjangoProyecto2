#imports
from django.urls import path, include
from . import views

app_name = 'microblog'

#configuracion
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.CustomSignUpView.as_view(), name='register')
]