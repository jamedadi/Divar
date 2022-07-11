from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from advertisement.models import Advertisement
from financial.models import Payment
from package.models import Package

user = get_user_model()


class Purchase(models.Model):
    """ 💰 """
    PAID = 10
    NOT_PAID = -10
    STATUS_CHOICES = (
        (PAID, _('Paid')),
        (NOT_PAID, _('Not Paid'))
    )
    user = models.ForeignKey(
        user, related_name='purchases', on_delete=models.SET_NULL, null=True, verbose_name=_('user')
    )
    package = models.ForeignKey(
        Package, related_name='purchases', on_delete=models.SET_NULL, null=True, verbose_name=_('package')
    )
    advertisement = models.ForeignKey(
        Advertisement, related_name='purchases', on_delete=models.SET_NULL, null=True, verbose_name=_('advertisement')
    )
    price = models.BigIntegerField(verbose_name=_('price'))
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NOT_PAID, verbose_name=_('status'))
    payment = models.ForeignKey(Payment, related_name='purchases', on_delete=models.PROTECT, verbose_name=_('payment'))

    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created_time'))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_('modified_time'))

    def __str__(self):
        return f"{self.user} >> {self.package}"

    class Meta:
        verbose_name = _('purchase')
        verbose_name_plural = _('purchases')

    @staticmethod
    def create_payment(package, user):
        """ 💾 """
        return Payment.objects.create(amount=package.price, user=user)

    @classmethod
    def create(cls, package, advertisement, user):
        """ 💾 """
        if package.is_enable:
            with transaction.atomic():
                payment = cls.create_payment(package=package, user=user)
                purchase = cls.objects.create(
                    package=package, user=user, price=package.price, payment=payment, advertisement=advertisement
                )
            return purchase
        return None
