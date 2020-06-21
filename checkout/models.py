from django.db import models

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
