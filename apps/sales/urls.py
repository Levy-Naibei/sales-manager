from django.urls import path

from . import views

urlpatterns = [
    path('create-customer/', views.CustomerCreateAPIView.as_view(), name="create-customer"),
    path('customers/', views.CustomerListAPIView.as_view(), name="get-customers"),
    path('orders/', views.OrderListAPIView.as_view(), name="get-orders"),
    path('create-order/', views.create_order, name="create-order"),
]
