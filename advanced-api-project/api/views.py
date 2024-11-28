from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book

#The purpose of this class is to List all available books.
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Creating a class for retrieving a book by its ID

class BookDetailView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


#Creating a class to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

#Creating a class to update an existing book
class BookUpdateView(generics.UpdateAPIView):
     queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

#creating a class to remove a book
class BookDeleteView(generics.DestroyAPIView):
     queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
