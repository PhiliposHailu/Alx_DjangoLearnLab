from django.shortcuts import render
from .models import Book

def books_list(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, "relationship_app/list_books.html", context)



from django.views.generic.detail import DetailView
from .models import Library

class DetailsOfSpecificLibrary(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'