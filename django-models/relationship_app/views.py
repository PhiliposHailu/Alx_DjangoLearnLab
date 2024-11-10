from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book

from django.contrib.auth import login 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

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