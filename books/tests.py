from django.test import TestCase
from django.urls import reverse
from .models import Book
import datetime

# Create your tests here.

class BookModelTest(TestCase):

    def setUp(self):
        # Create some test data
        Book.objects.create(
            name="Book for Testing",
            author="Test Author",
            published="2025-02-12",
            pages=9999,
            price=999,
            description="A Django book",
        )

    def test_book_creation(self):
        book = Book.objects.get(name="Book for Testing")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.published, datetime.date(2025, 2, 12))
        self.assertEqual(book.pages, 9999)
        self.assertEqual(book.price, 999)
        self.assertEqual(book.description, "A Django book")
