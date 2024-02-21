from django.contrib.auth import get_user_model
from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

User = get_user_model()

class CustomerCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    # permission_classes= [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(name=request.user)
        return Response(
            {"message": "Customer successfully created"},
            status=status.HTTP_201_CREATED,
        )


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all().order_by("-created_at")
    serializer_class = CustomerSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    # permission_classes= [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=request.user)
        return Response(
            {"message": "Order successfully created"}, status=status.HTTP_201_CREATED
        )
    