from django.contrib import admin
from .models import Category



@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ('name', 'parent')
    list_display = ('name', 'parent')
    list_display_links = ('name', 'parent')
