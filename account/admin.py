from codecs import register
from django.contrib import admin
from .models import User


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    pass



