from django.contrib import admin
from .models import Category, Menu

# Register your models here.
admin.site.register(Menu)
admin.site.register(Category)