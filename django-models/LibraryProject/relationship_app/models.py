from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=25)  
    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=25)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")  
    def __str__(self):
        return f"{self.title} written by {self.author}"


class Library(models.Model):
    name = models.CharField(max_length=25)  
    books = models.ManyToManyField(Book, related_name="libraries")  
    def __str__(self):
        return f"{self.name}"  


class Librarian(models.Model):
    name = models.CharField(max_length=25)  
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")  
    def __str__(self):
        return f"{self.name} works in {self.library}"

