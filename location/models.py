from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.base_model import BaseModel


class Province(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, allow_unicode='True', verbose_name=_('slug'))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'province'
        verbose_name_plural = 'provinces'


class City(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, allow_unicode='True', unique=True, blank=True, verbose_name=_('slug'))
    state = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE, verbose_name=_('state'))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class District(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=50, allow_unicode='True', verbose_name=_('slug'))
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE, verbose_name=_('city'))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')


class Location(BaseModel):
    """
    This model represents location of published advertisement by User
    """
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name=_('province'))
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name=_('city'))
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('district'))

    def __str__(self):
        return f"{self.city} < {self.province}"

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _("locations")
