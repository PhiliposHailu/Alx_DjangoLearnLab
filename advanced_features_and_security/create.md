from bookshelf.models import Book
book1 = Book(title='1984', author='George Orwell', publication_year=1949)
book1.save()

#Expexted ouput: successful creation of a new book instance
#(No output if creation of the instance is successful)
