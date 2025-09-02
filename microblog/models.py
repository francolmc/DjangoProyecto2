from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

#TODO: Crear clase de users
class Users(models.Model):
    name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=320, blank=False, unique=True)
    password = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#TODO: Crear clase de posts
class Posts(models.Model):
    content = models.CharField(max_length=140, blank=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories)
    created_at = models.DateTimeField(auto_now_add=True)

#TODO: Crear clase de likes
class Likes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#TODO: Crear clase de comments
class Comments(models.Model):
    content = models.CharField(max_length=140, blank=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)