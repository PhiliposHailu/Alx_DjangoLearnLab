from django.urls import path
from .views import views, list_books

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk', views.LibraryDetailView.as_view(), name='library_detail'),
]