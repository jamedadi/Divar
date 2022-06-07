import uuid

from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import ugettext_lazy as _


user = get_user_model()

class Gateway(models.Model):

    FUNCTION_ZARINPAL = 'zarinpal'

    GATEWAY_FUNCTION = (
        (FUNCTION_ZARINPAL, 'Zarinpal'),
    )

    title = models.CharField(max_length=180, verbose_name=_('gateway title'))
    gateway_request_url = models.CharField(max_length=150, verbose_name=_('request url'), null=True, blank=True)
    gateway_verify_url = models.CharField(max_length=150, verbose_name=_('verify url'), null=True, blank=True)
    gateway_code = models.CharField(max_length=12, verbose_name=_('gateway code'), choices=GATEWAY_FUNCTION)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    auth_data = models.TextField(verbose_name=_('auth data'), null=True, blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Gateway')
        verbose_name_plural = _('Gateways')

    def __str__(self):
        return self.title


class Payment(models.Model):

    invoice_number = models.UUIDField(max_length=150, verbose_name=_('invoice number'), default=uuid.uuid4())
    amount = models.IntegerField(verbose_name=_('amount'))
    gateway = models.ForeignKey(
        Gateway,related_name='payments', verbose_name=_('gateway'), on_delete=models.CASCADE, null=True
    )
    is_paid = models.BooleanField(verbose_name=_('is paid'), default=False)
    payment_log = models.TextField(verbose_name=_('log'), blank=True)
    user = models.ForeignKey(user, related_name='payments', verbose_name=_('user'), on_delete=models.SET_NULL, null=True)
    authority = models.CharField(max_length=64, verbose_name=_('authority'), blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return self.invoice_number.hex

