from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    slug = models.SlugField(max_length=200, null=True, blank=True, allow_unicode=True, verbose_name=_('slug'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _("categories")
