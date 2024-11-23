from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerializer(serializers.odelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
