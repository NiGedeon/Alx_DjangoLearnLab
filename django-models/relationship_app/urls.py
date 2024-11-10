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
]