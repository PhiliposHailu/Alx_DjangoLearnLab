from django.contrib import admin
from .models import Book

class BooAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
    ordering = ('title',)

admin.site.register(Book, BooAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )
    
admin.site.register(CustomUser, CustomUserAdmin)



from django import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/<int:book_id>/', views.view_book, name='view_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/add/', views.add_book, name='add_book'),
]