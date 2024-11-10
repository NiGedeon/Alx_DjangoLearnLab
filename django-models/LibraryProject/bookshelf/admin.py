from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
     # Displaying the fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Adding a filter by publication year
    list_filter = ('publication_year',)

    # Enabling search functionality for title and author fields
    search_fields = ('title', 'author')

# Registering the Book model with the customized admin class
admin.site.register(Book, BookAdmin)

# Register your models here.
