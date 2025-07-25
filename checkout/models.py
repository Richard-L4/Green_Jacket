import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from items.models import Item
from profiles.models import UserProfile


class Order(models.Model):
    """
    Model representing a customer's order.
    Stores customer details, delivery cost, total, and Stripe PID.
    """
    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_trolley = models.TextField(
        null=False, blank=False, default=''
    )
    stripe_pid = models.CharField(max_length=254, null=True, blank=True)

    def _generate_order_number(self):
        """
        Generate a unique, random order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total after each item addition or change.
        Applies delivery cost if below free threshold.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override default save method to assign order number
        if it hasn’t already been set.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Individual line item within an order.
    Stores item, quantity, size (if any), and computed line total.
    """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems'
    )
    item = models.ForeignKey(
        Item, null=False, blank=False, on_delete=models.CASCADE
    )
    item_size = models.CharField(
        max_length=2, null=True, blank=True
    )  # e.g., XS, S, M, L, XL
    quantity = models.IntegerField(
        null=False, blank=False, default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override save method to calculate line total
        and trigger update to the order total.
        """
        self.lineitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'SKU {self.item.sku} on order {self.order.order_number}'
        )
