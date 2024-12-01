from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAuthorAPITestCase(APITestCase):
    def setUp(self):
        # Create an author
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books associated with authors
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author2)

        # Define URLs
        self.authors_url = '/api/authors/'
        self.books_url = '/api/books/'


def test_get_authors(self):
    response = self.client.get(self.authors_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)  # Verify two authors are returned

