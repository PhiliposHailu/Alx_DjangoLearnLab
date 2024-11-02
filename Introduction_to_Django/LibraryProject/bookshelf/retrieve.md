all_books = Book.objects.all()
for book in all_books:
    print(book.title, book.author, book.publication_year)
    
#Expexted ouput:
#1984 George Orwell 1949
