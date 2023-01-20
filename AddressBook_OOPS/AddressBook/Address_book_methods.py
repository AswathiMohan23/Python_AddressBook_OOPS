

class Address_book_methods(object):
    def __init__(self, contact, addressBook):
        self.contact = contact
        self.addressBook = addressBook

    def adding_data_from_console(self, contact):
        print("\n ------------------------------------------ UC5 (refactored UC2 to add multiple contacts) ----------------------------------------------------------------------\n")
        limit = int(input("Enter the no of contacts you need to add to the contact book : "))
        for i in range(0, limit):
            print("\nenter the details of contact ", i)
            data = self.adding_details()
            contact.append(data)

    def display_contactBook( self,contact):
        print("\n\t\t\t\t\t---------------- Existing contact book ------------------------ \n\n", contact)

    def adding_details(self):
        first_name = input("Enter the first name : ")
        second_name = input("Enter the second name : ")
        address = input("Enter the address : ")
        city = input("Enter the city : ")
        state = input("Enter the state : ")
        zip_code = input("Enter the zip_code : ")
        phn = input("Enter the phone number : ")
        email = input("Enter the email : ")
        data = {"first_name": first_name, "second_name": second_name, "address": address, "city": city, "state": state,
                "zip_code": zip_code, "phn": phn, "email": email}
        return data

    def edit_data(self, contact):
        print("\n ------------------------------------------------------ UC3 ----------------------------------------------------------------------\n")
        name_to_be_edited = input("enter the first name to edit the contact : ")
        for i in contact:
            for j in i:
                if i.get(j) == name_to_be_edited:
                    data = self.adding_details()
                    i.update(data)

    def delete_contact(self, contact):
        print("\n ------------------------------------------------------ UC4 ----------------------------------------------------------------------\n")
        name_to_be_deleted = input("enter the first name of the person whose details should be deleted : ")
        for k in contact:
            for j in k:
                if k.get(j) == name_to_be_deleted:
                    contact.remove(k)
                    self.after_deletion(contact, name_to_be_deleted)

    def after_deletion(self, contact, name):
        print("\n******************************* After deleting details of", name, " ******************************\n")
        self.display_contactBook(contact)

    def get_value(self, lst, key, value):
        for i, contact in enumerate(lst):
            if contact[key] == value:
                data = self.adding_details();
                return data

    def multiple_addressBook(self, addressBook):
        limit = int(input("Enter the number of address books you need : "))

        for i in range(0, limit):
            multiple_contact = []
            print("\n\t\t\t ========>   AddressBook", i)
            number = int(input("\nEnter the no of contacts you need to add to the address book : "))
            for j in range(0, number):
                contact1 = []

                print("\n\t\t\tcontact", j, " of AddressBook ", i)
                data = self.adding_details()
                multiple_contact.append(data)
                contact1.append(multiple_contact)
                addressBook.update({i: contact1})


# ------------------------------------------------------------------------------------------------------------------------
