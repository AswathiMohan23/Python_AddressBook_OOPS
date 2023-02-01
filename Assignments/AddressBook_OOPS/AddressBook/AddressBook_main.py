from Address_book_methods import *

print("\n\t\t\t\t\t\t\t\t\t WELCOME TO ADDRESSBOOK \n\t\t\t\t\t\t\t\t  ***************************\n")

contact = []
addressBook = {}
address = Address_book_methods(contact,addressBook)
#address = Address_book_methods()
address.adding_data_from_console(contact)
address.display_contactBook(contact)
address.edit_data(contact)
address.display_contactBook(contact)
address.delete_contact(contact)
print("\n\n printing list using iterator : ")
length = len(contact)
iterator = iter(contact)
print(next(iterator))
address.multiple_addressBook(addressBook)
address.display_contactBook(addressBook)
