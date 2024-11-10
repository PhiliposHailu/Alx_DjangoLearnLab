from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

def book_list(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Inject additional context data - list of books in the library."""
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all() 
        return context