import uuid
from django.db import models
from django.db.models import Sum
from products.models import Product

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Returns a random string for an order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Runs to update the total based on item price times quantity
        (if quantity)
        """
        self.order_total = self.lineitems.aggregate(
            Sum('line_total'))['line_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Save the order to the DB and makes sure it has an order number.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns order number.
        """
        return self.order_number


class OrderLine(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Saves the line quantity if applicable to the order
        """
        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns product name and order number. 
        """
        return f'item {self.product.name} on order {self.order.order_number}'
