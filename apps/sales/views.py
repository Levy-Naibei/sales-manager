from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

User = get_user_model()


class CustomerCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Customer successfully created"},
            status=status.HTTP_201_CREATED,
        )


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all().order_by("-created_at")
    serializer_class = CustomerSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data
    customer_name = get_object_or_404(Customer, id=data.get("customer"))
    order = Order.objects.create(
        customer=customer_name, item=data.get("item"), amount=data.get("amount")
    )
    serializer = OrderSerializer(data=order)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Customer successfully created", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer


# class OrderCreateAPIView(generics.CreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 {"message": "Customer successfully created"},
#                 status=status.HTTP_201_CREATED,
#             )
#         print("===== ", serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
