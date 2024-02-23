from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.sales.models import Customer


class SalesTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create test data for a customer
        self.customer = Customer.objects.create(
            name="John Doe", phone_number="+254704590344", email="johndoe@gmail.com"
        )

        # create test data fro order
        # self.order = {
        #     "customer": self.customer.id,
        #     "item": "macbook m2",
        #     "amount": "40000.56",
        # }

    def test_create_customer(self):
        url = reverse("create-customer")
        client = APIClient()
        client.force_login(self.user)
        data = {
            "name": "Jane Doe",
            "phone_number": "+254704590344",
            "email": "johndoe@gmail.com",
        }
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    # def test_create_order(self):
    #     url = reverse("create-order")
    #     client = APIClient()
    #     client.force_login(self.user)
    #     response = client.post(url, self.order, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
