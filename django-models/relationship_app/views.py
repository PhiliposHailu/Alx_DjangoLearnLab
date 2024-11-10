from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book

from django.contrib.auth import login 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


def check_role(role):
    return lambda u: u.userprofile.role == role

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return HttpResponse("Welcome Admin!")

def admin_view_with_error(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Or redirect to the login page
    elif request.user.userprofile.role != 'Admin':
        return render(request, 'relationship_app/admin_view.html')  # Access Denied page
    return HttpResponse("Welcome Admin!")


@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return HttpResponse("Welcome Librarian!")

def librarian_view_with_error(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Or redirect to the login page
    elif request.user.userprofile.role != 'Librarian':
        return render(request, 'relationship_app/librarian_view.html')  # Access Denied page
    return HttpResponse("Welcome Librarian!")


@user_passes_test(check_role('Member'))
def member_view(request):
    return HttpResponse("Welcome Member!")

def member_view_with_error(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Or redirect to the login page
    elif request.user.userprofile.role != 'Member':
        return render(request, 'relationship_app/member_view.html')  # Access Denied page
    return HttpResponse("Welcome Member!")



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
    

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            login(request, user) 
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


