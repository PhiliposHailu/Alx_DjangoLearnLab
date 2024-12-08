from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', name='login')),
    path('logout/', auth_views.LogoutView.as_view(name='logout')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.BlogListView.as_view(), name='list_of_books'),
    path('posts/new/', views.BlogCreateView.as_view(), name='blog_post_creation'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='detail_view_of_posts'),
    path('posts/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='editing_posts'),
    path('posts/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete_post'),
]

