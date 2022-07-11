from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from financial.models import Payment


@receiver(post_save, sender=Payment)
def callback(sender, instance, created, **kwargs):
    """
    Signal to update the status 🚦 of the purchase 💰 after payment 💸 is made
    """
    if instance.is_paid and not instance._b_is_paid:
        if instance.purchases.exists():
            purchase = instance.purchases.first()
            purchase.status = purchase.PAID
            purchase.save()


@receiver(post_init, sender=Payment)
def store_is_paid_status(sender, instance, **kwargs):
    """
    Signal to store the status 🚦 of the purchase 💰 before payment 💸 is made
    """
    instance._b_is_paid = instance.is_paid
