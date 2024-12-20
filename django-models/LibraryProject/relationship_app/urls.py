# from django.urls import path
# from . import views
# from .views import list_books
# from .views import CustomLoginView, CustomLogoutView, RegisterView

# urlpatterns = [
#    path('books/', views.list_books, name='list_books'),  
#    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
#    path('login/', CustomLoginView.as_view(), name='login'),
#    path('logout/', CustomLogoutView.as_view(), name='logout'),
#    path('register/', RegisterView.as_view(), name='register'),
# ]


from django.urls import path
from . import views
from .views import list_books
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
