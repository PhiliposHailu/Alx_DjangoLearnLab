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



from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'
def check_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'
def check_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin Page!")
@user_passes_test(check_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Page!")
@user_passes_test(check_member)
def member_view(request):
    return HttpResponse("Welcome to the Member Page!")
