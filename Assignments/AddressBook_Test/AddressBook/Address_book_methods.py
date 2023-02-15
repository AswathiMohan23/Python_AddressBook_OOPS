from Details import Details
from AddressBookException import AddressBookException


class Address_book_methods(Details):
    def __init__(self, contact, addressBook):
        self.contact = contact
        self.addressBook = addressBook
        self.temp=None


    def adding_data_from_console(self, contact):
        print(
            "\n ------------------------------------------ UC5 (refactored UC2 to add multiple contacts) ----------------------------------------------------------------------\n")
        limit = int(input("Enter the no of contacts you need to add to the contact book : "))
        for i in range(0, limit):
            print("\nenter the details of contact ", i)
            data = self.adding_details()
            contact.append(data)

    def display_contactBook(self, contact):
        print("\n\t\t\t\t\t---------------- Existing contact book ------------------------ \n\n", contact)
        '''print("  FirstName  ", "  LastName  ", "  Address  ", "  City  ", "  State  ", "  Zip_code  ", "  PhoneNumber  ",
              "  email  ")

        for i in contact:
            for key, value in i.items():
                print(value, end='\t \t')'''

    def adding_details(self):

        self.setFirst_name(input("Enter the first name : "))
        self.setLast_name(input("Enter the second name : "))
        self.setAddress(input("Enter the address : "))
        self.setCity(input("Enter the city : "))
        self.setState(input("Enter the state : "))
        self.setZip_code(input("Enter the zip_code : "))

        try:
            self.setEmail(input("Enter the email : "))
            self.temp = (int(input("Enter the phone number : ")))
            print(type(self.temp))
            if type(self.temp) != int:
                print(type(self.getPhn()))
                raise AddressBookException
            else:
                self.setPhn(self.temp)
        except AddressBookException:
            print("Invalid type... ")
        except ValueError:
            print("Invalid")



        data = {"first_name": self.getFirst_name(), "second_name": self.getLast_name(),
                "address": self.getAddress(), "city": self.getCity(), "state": self.getState(),
                "zip_code": self.getZip_code(), "phn": self.getPhn(), "email": self.getEmail()}
        return data

    def edit_data(self, contact):
        print(
            "\n ------------------------------------------------------ UC3 ----------------------------------------------------------------------\n")
        name_to_be_edited = input("enter the first name to edit the contact : ")
        for i in contact:
            for j in i:
                if i.get(j) == name_to_be_edited:
                    data = self.adding_details()
                    i.update(data)

    def delete_contact(self, contact):
        print(
            "\n ------------------------------------------------------ UC4 ----------------------------------------------------------------------\n")
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
details = Details()
