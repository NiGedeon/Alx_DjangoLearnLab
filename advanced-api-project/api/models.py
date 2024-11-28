from django.db import models

#This class is used to make a Table to hold the records of the Author Model

class Author(models.Model):
    name = models.CharField(max_length = 30)

#This class is used to make a Table to hold the records of the Book Model
class Book(models.Model):
    title = models.CharField(max_length = 255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = "author")
