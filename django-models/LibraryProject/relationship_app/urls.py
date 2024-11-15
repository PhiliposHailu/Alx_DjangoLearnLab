from urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'), 
]