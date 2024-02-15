from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Customer, Order

# @admin.register(Customer)
# class CustomerAdmin(BaseUserAdmin):
#     list_display = ["name", "code", "phone_number"]
#     list_filter = ["code"]
    
# @admin.register(Order)
# class OrderAdmin(BaseUserAdmin):
#     list_display = ["item", "amount", "date_ordered"]
#     list_filter = ["item", "date_ordered"]

admin.site.register(Customer)
admin.site.register(Order)
