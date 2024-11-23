from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer        

class BookViewSet(viewsets.ModelViewSet):
    # authentication is being checked
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
