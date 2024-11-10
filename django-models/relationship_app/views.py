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

from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

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
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, "relationship_app/register.html", {'form': form})


def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin View
@user_passes_test(lambda user: user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian View
@user_passes_test(lambda user: user.userprofile.role == 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(lambda user: user.userprofile.role == 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
