from bookshelf.models import Book
# Deleting the book created
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm the deletion by retrieving all books
Book.objects.all()
