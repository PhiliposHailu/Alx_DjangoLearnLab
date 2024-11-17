
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book
from .forms import ExampleForm  # Import the form



@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    book_list = ", ".join([book.title for book in books])
    return HttpResponse(f"Books: {book_list}")

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        book = Book.objects.create(title=title, author=author, publication_year=publication_year)
    return HttpResponse(f"{book.title} added successfully")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
    return HttpResponse(f" Book edited to {book.title} successfully")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
    return HttpResponse(f" Book deleted successfully")


def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title_icontains=query)
    return render(request, 'bookshelf/book_list.html',{'books': books})


def search_books(request):
    form = ExampleForm(request.GET)  # Bind query parameters to the form
    if form.is_valid():  # Validate the form
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)  # Safe ORM query
    else:
        books = Book.objects.none()  # Return an empty queryset if invalid
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
