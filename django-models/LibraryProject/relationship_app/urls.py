from urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('register/', views.register, name='register'),  
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]



from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin', views.admin_view, name='admin_view'),
    path('librarian', views.admin_view, name='librarian_view'),
    path('member', views.admin_view, name='member_view'),
]
