from django.db import models
from django.utils.translation import ugettext_lazy as _


class Package(models.Model):
    title = models.CharField(max_length=48, verbose_name=_('package title'))
    price = models.PositiveBigIntegerField(verbose_name=_('package price'))
    description = models.TextField(blank=True, verbose_name=_('package description'))
    days = models.PositiveSmallIntegerField(verbose_name=_('package days'))
    is_enable = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

