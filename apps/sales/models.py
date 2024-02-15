import random
import string

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Customer(TimeStampedUUIDModel):
    name = models.ForeignKey(
        User,
        verbose_name=_("Customer Name"),
        related_name="customer",
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        verbose_name=_("Customer Code"),
        max_length=255,
        unique=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+254710311897"
    )
    
    def __str__(self):
        return f"{self.name.first_name.title()} {self.name.last_name.title()}"

    # generate random code on model instance save
    def save(self, *args, **kwargs):
        self.code = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=8)
        )
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Order(TimeStampedUUIDModel):
    customer = models.ForeignKey(
        Customer, related_name="order", on_delete=models.CASCADE
    )
    item = models.CharField(
        verbose_name=_("Product"), max_length=30, null=False, blank=False
    )
    amount = models.DecimalField(
        verbose_name=_("Price"), max_digits=8, decimal_places=2, default=0.0
    )
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
