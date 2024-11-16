update_book = Book.objects.get(title='1984')
update_book.title='Nineteen Eighty-Four'
updat_book.save()

#Expexted ouput:
#Nineteen Eighty-Four George Orwell 1949
