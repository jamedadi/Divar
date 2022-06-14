from django.contrib import admin
from django.contrib.admin import register

from purchase.models import Purchase


@register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "package", "price", "status", "created_time")
    list_filter = ("status",)
    search_fields = ("user__username", "package__name")
