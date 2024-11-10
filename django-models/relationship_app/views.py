from django.shortcuts import render
from . import Book, Author, Library, Librarian

def Books(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'relationship_app/book_list.html', context)