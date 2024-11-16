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


from django.contrib.auth import login