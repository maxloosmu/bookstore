from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Order, Book

# Create your tests here.

class CartViewTest(TestCase):

    def test_cart_page_status_code(self):
        response = self.client.get(reverse('cart.index'))
        self.assertEqual(response.status_code, 200)

# Testing unauthenticated purchase requires login
class PurchaseAuthTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            name="Test Book",
            author="Author",
            published="2025-02-12",
            pages=100,
            price=50,
            description="For purchase test"
        )

    def test_purchase_requires_login(self):
        response = self.client.post(reverse('cart.purchase'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/login/' in response.url)

# Testing cart and purchase with an authenticated user
class PurchaseTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.book = Book.objects.create(
            name="Test Book",
            author="Author",
            published="2025-02-12",
            pages=100,
            price=50,
            description="For purchase test"
        )

    def test_cart_page_status_code(self):
        response = self.client.get(reverse('cart.index'))
        self.assertEqual(response.status_code, 200)

    def test_purchase_creates_order(self):
        # Add an item to the cart
        response = self.client.post(reverse('cart.add', args=[self.book.id]), {'quantity': 1})
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect to cart.index due to the add() view/function

        # Check session cart
        session = self.client.session
        print("Cart contents:", session.get('cart'))

        # Simulate checkout
        response = self.client.post(reverse('cart.purchase'))
        print("Purchase response status:", response.status_code)

        # 200 because purchase() view renders template
        self.assertEqual(response.status_code, 200)

        # Verify an Order was created
        self.assertEqual(Order.objects.count(), 1)
