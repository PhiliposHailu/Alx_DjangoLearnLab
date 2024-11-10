from bookshelf.models import Book
Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

#Expexted ouput: successful creation of a new book instance
#(No output if creation of the instance is successful)
