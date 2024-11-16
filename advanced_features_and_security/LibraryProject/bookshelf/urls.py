from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('create/', views.create_user, name='create_user'),
    path('books/', views.book_list, name='book_list'),
]

