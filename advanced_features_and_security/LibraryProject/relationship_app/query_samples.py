

from .models import Book, Author, Library, Librarian


    # Query all books by a specific author.
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)

        print(f"books authored by {author_name}")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"No author found withe the name: {author_name}")


    # List all books in a library.
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()

        print(f"books in {library_name} library.")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")


    # Retrieve the librarian for a library.
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"librarian:  {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")
