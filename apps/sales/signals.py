import africastalking
from django.db.models.signals import post_save
from django.dispatch import receiver

from screening_test.settings import env
from .models import Order

username=env("AFRICASTALKING_USERNAME")
api_key=env("AFRICASTALKING_API_KEY")
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@receiver(post_save, sender=Order)
def send_sms_on_order_creation(sender, instance, created, **kwargs):
    if created:
        customer_phone_number = f"{instance.customer.phone_number}"
        customer_name = f"{instance.customer.name.title()}"
        price = f"{instance.amount}"
        product = instance.item
        message = f"Dear {customer_name}, your order for {product} costing KES {price}" \
                  f" has been created successfully. Thank you for choosing us!"
        
        response = sms.send(message, [customer_phone_number])
        print(response)
        

