from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAuthorAPITestCase(APITestCase):
    def setUp(self):

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Log in the test user
        self.client.login(username='testuser', password='testpass')

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

def test_create_author(self):
    data = {"name": "New Author"}
    response = self.client.post(self.authors_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Author.objects.count(), 3)  # Verify new author is added

def test_delete_author(self):
    url = f'{self.authors_url}{self.author1.id}/'
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Author.objects.count(), 1)  # Verify author is deleted

def test_get_books(self):
    response = self.client.get(self.books_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)  # Verify two books are returned


def test_create_book(self):
    data = {"title": "New Book", "publication_year": 2022, "author": self.author1.id}
    response = self.client.post(self.books_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)  # Verify new book is added


def test_update_book(self):
    url = f'{self.books_url}{self.book1.id}/'
    data = {"title": "Updated Book", "publication_year": 2023, "author": self.author2.id}
    response = self.client.put(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book1.refresh_from_db()
    self.assertEqual(self.book1.title, "Updated Book")

def test_delete_book(self):
    url = f'{self.books_url}{self.book1.id}/'
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 1)  # Verify book is deleted

