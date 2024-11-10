from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from . models import Book,Library
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
