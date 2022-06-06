from django.contrib.auth import get_user_model
from django.db import models

from financial.models import Payment
from package.models import Package

user = get_user_model()


class Purchase(models.Model):
    PAID = 10
    NOT_PAID = -10
    STATUS_CHOICES = (
        (PAID, 'Paid'),
        (NOT_PAID, 'Not Paid')
    )
    user = models.ForeignKey(user, related_name='purchases', on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(Package, related_name='purchases', on_delete=models.SET_NULL, null=True)
    price = models.BigIntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NOT_PAID)
    payment = models.ForeignKey(Payment, related_name='purchases', on_delete=models.PROTECT)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} >> {self.package}"