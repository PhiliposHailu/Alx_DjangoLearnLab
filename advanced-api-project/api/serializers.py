from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

#serializes all the fields of the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        cur_year = datetime.now().year
        if data['publication_year'] > cur_year:
            raise serializers.ValidationError("The year must not be greater than current year.")

#serializes all the fields of the Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = "__all__"
    
    
