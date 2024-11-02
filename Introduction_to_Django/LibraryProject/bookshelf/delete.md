delete_book = Book.objects.get(title='Nineteen Eighty-Four')
delete_book.delete()

book = Book.objects.all()
print(book.title, book.author, book.publication_year)

#Expexted ouput:
#(1, {'bookshelf.Book': 1})
