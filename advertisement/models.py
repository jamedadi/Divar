from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


from category.models import Category
from lib.base_model import BaseModel
from lib.username import generate_random_string
from location.models import Location

# To get user from settings
User = get_user_model()


class Advertisement(BaseModel):
    """
    This class represents Advertisement model.
    Each user can one or more advertisement to publish 📢
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='advertisements',)
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('description'))
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='advertisements', verbose_name=_('location')
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="advertisements", verbose_name=_('category')
    )

    def __str__(self):
        return f"{self.title} > {self.location.city.name}"

    class Meta:
        verbose_name = _('advertisement')
        verbose_name_plural = _("advertisements")

    @classmethod
    def add(cls, user, title, description, price, location, category, images):
        """
        Get data an Advertisement and Save it in Database 💾
        """
        adv = cls.objects.create(user=user,
                                 title=title,
                                 description=description,
                                 price=price,
                                 location=location,
                                 category=category)
        for file in images:
            adv.images.create(name=generate_random_string(), image_file=file)
        adv.save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('advertisement-detail', args=[str(self.pk)])

    @classmethod
    def is_belong_user(cls, user, advertisement_pk):
        """To check this advertisement posted by this user or not"""
        advertisement = cls.objects.get(pk=advertisement_pk)
        return user == advertisement.user


class AdvertisementImage(BaseModel):
    """
    This class represents Image model.
    Each advertisement has one or many images. 🖼
    """
    name = models.CharField(max_length=50, verbose_name=_('name'))
    advertisement = models.ForeignKey(
        Advertisement, on_delete=models.CASCADE, related_name='images', verbose_name=_('advertisement')
    )
    image_file = models.FileField(
            upload_to='images/advertisement/',
            validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg'))],
            verbose_name=_('images')
            )



class Attribute(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('attribute'))


class AdvAttrValue(models.Model):
    advertisement = models.ForeignKey(
        Advertisement, on_delete=models.CASCADE, related_name='attributes', verbose_name=_('advertisement')
    )
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name='attributes', verbose_name=_('attribute')
    )
    value = models.CharField(max_length=50, verbose_name=_('value'))
