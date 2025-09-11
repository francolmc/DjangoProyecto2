from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#TODO: Crear clase de users
class CustomUsers(AbstractUser):
    personal_url = models.TextField()

#TODO: Crear clase de posts
class Posts(models.Model):
    content = models.CharField(max_length=140, blank=False)
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#TODO: Crear clase de likes
class Likes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#TODO: Crear clase de comments
class Comments(models.Model):
    content = models.CharField(max_length=140, blank=False)
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)