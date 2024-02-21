from rest_framework import serializers

from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"
    
    def get_customer(self, obj):
        return obj.customer.name
    