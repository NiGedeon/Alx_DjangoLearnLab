from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class BookSerializer(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
