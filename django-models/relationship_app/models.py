from django.db import models

# Create your models here.
 
class Author(models.Model):
    name = models.charField(max_length= 200)

class Book(models.Model):
    title = models.charField(max_length= 200)
    author = models.ManyToManyField(Author, related_name= "books")

class Library(models.Model):
    name = models.charField(max_length= 200)
    books = models.ManyToManyField(Book, related_name= "libraries")

class Librarian(models.Model):
    name = models.charField(max_length= 200)
    library = models.ManyToManyField(Book, related_name= "librarians")