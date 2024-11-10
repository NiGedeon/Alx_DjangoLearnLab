from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from . models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Login view using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout view using Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

# Registration view to handle user sign-up
class RegisterView(View):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})

