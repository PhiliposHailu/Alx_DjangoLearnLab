from django.shortcuts import render
from .models import Book


def list_books(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, "relationship_app/list_books.html", context)



from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = Library.books.all()
        return context

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfuly created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form' : form})



from django.contrib.auth.decorators import user_passes_test


def check_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'
def check_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'
def check_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        book = Book.objects.create(title=title, author=author, publication_year=publication_year)
    return HttpResponse(f"{book.title} added successfully")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
    return HttpResponse(f" Book edited to {book.title} successfully")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
    return HttpResponse(f" Book deleted successfully")
