delete_book = Book.objects.get(title='Nineteen Eighty-Four')
delete_book.delete()

all_books = Book.objects.all()
for book in all_books:
    print(book.title, book.author, book.publication_year)

#Expexted ouput:
#(1, {'bookshelf.Book': 1})
