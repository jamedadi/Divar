from django.contrib import admin
from .models import Advertisement, AdvertisementImage


class AdvertisementImageInline(admin.TabularInline):
    model = AdvertisementImage


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    inlines = [AdvertisementImageInline]
    # list_select_related = ('images', )


#
# @admin.register(AdvertisementImage)
# class AdvertisementImageAdmin(admin.ModelAdmin):
#     pass
