from django.contrib import admin
from .models import Categories, CustomUsers

# Register your models here.
admin.site.register(Categories)
admin.site.register(CustomUsers)