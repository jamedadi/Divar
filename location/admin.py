from django.contrib import admin
from .models import Location, Province, City, District


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass



@admin.register(District)
class DistinctAdmin(admin.ModelAdmin):
    pass





