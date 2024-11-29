from django.urls import path
from .views import CreateView, UpdateView, DeleteView, DetailView, ListView

urlpattern = [
    path('books/', ListView.as_view(), name='list_of_books'),
    path('books/<int:pk>/', DetailView.as_view(), name='book_details'),
    path('books/create', CreateView.as_view(), name='create_a_book'),
    path('books/update/', UpdateView.as_view(), name='update_a_book'),
    path('books/delete/', DeleteView.as_view(), name='delete_a_book'),
]