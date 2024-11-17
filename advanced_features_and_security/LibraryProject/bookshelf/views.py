
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    books_list = ", ".join([book.title for book in books])
    return HttpResponse(f"Books: {books_list}")

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