from django.urls import path

from . import views

urlpatterns = [
    path('create-customers/', views.CustomerCreateAPIView.as_view(), name="customer-create"),
    path('customers/', views.CustomerListAPIView.as_view(), name="get-customers"),
    path('orders/', views.OrderListAPIView.as_view(), name="get-orders"),
    path('create-orders/', views.OrderCreateAPIView.as_view(), name="order-create"),
]
