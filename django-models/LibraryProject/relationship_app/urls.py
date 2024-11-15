from urls import path
from .views import books_list, DetailsOfSpecificLibrary
from . import views

urlpatterns = [
    path('books/', views.books_list, name='book_list'), 
]