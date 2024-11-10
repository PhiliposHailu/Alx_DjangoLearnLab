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

def books_in_library(library_name):
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        # Get all books associated with this library
        books = library.books.all()
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")

def librarian_for_library(library_name):
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        # Retrieve all librarians for this library
        librarians = Librarian.objects.get(library=library)
        print(f"Librarians for {library_name} library:")
        for librarian in librarians:
            print(f"- {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")git