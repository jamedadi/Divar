from django.contrib import admin
from django.contrib.admin import register

from financial.models import Gateway, Payment


@register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ("title", "is_enable", "created_time")
    list_filter = ("is_enable",)
    search_fields = ("title",)


@register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_number",
        "amount",
        "user",
        "gateway",
        "is_paid",
        "created_time",
    )
    list_filter = ("is_paid", "gateway")
    search_fields = ("user__username", "gateway__name")
