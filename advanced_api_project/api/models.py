from django.db import models


class Author(models):
    name = models.CharField(max_length=20)

class Book(models):
    title = models.CharField(max_length=50)
    publication_year = models.DateTimeField(auto_now=True)
    author = models.ManyToOneRel(Author, on_delete=models.SET_DEFAULT, related_name='books')


