from django.db import models

from lib.base_model import BaseModel


class Province(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, allow_unicode='True')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'


class City(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, allow_unicode='True')
    state = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class District(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, allow_unicode='True')
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"


class Location(BaseModel):
    """
    This model represents location of published advertisement by User
    """
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.city} < {self.province}"

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
