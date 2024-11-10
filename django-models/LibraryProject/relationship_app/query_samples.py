#Query all books by a specific author
author = Author.objects.get(authorName = name)
books_by_author = Book.objects.filter(author = author)

#List all books in a library.
library = Library.objects.get(name = name)
books_in_library = library.books.all()

#Retrieve the librarian for a library.
library = Librarian.objects.get(name=name)
librarian = library.name
