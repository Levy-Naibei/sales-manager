from rest_framework import serializers

from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField() 

    class Meta:
        model = Customer
        fields = "__all__"
    
    def get_name(self, obj):
        return obj.name.username

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"
    
    def get_customer(self, obj):
        return obj.customer.name.username
    