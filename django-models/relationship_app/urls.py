from django.urls import path
from .views import list_books, admin_view_with_error, librarian_view_with_error, member_view_with_error, views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin_view_with_error, name='admin_view'),
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('librarian/', librarian_view_with_error, name='librarian_view'),
    path('member/', member_view_with_error, name='member_view'),
]