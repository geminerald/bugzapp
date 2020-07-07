from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLine


@receiver(post_save, sender=OrderLine)
def update_on_save(sender, instance, created, **kwargs):
    """
    updates and order total on a line item in the order
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLine)
def update_on_delete(sender, instance, **kwargs):
    """
    updates and order total on a line item delete
    """
    print("delete signal received")
    instance.order.update_total()
