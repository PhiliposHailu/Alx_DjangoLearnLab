from . import Book, Author, Library, Librarian

def books_by_author(author_name):
    try:
        # Get the author by name
        author = Author.objects.get(name=author_name)
        # Get all books by this author
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name: {author_name}")
