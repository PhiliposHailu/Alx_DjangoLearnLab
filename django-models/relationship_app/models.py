from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    ROLE_Pick = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_Pick)
    def __str__(self):
        return f'{self.user.username} - {self.role}'



class Author(models.Model):
    name = models.charField(max_length= 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.charField(max_length= 200)
    author = models.ManyToManyField(Author, related_name= "books")

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.charField(max_length= 200)
    books = models.ManyToManyField(Book, related_name= "libraries")

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.charField(max_length= 200)
    library = models.ManyToManyField(Book, related_name= "librarians")
    
    def __str__(self):
        return self.name

