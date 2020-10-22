# Dunder methods

# class Phone():
#     spanish_name = 'telefono'
#     objs_count   = 0
#     def __init__(self, brand, size, adapter_type):
#         self.brand          = brand
#         self.size           = size
#         self.adapter_type   = adapter_type
#         Phone.objs_count += 1
#         if Phone.objs_count % 100 == 0:
#             Phone.anniversary()
#     @classmethod # Decorator
#     def anniversary(cls):
#         print(f"Happy birthday to Phone, so far, {cls.objs_count} objects have been created")
#     def __str__(self):
#         """
#         User friendly displayed name
#         """
#         return f'{self.brand} Phone ({self.size}")'
#     def __repr__(self):
#         """
#         Dev friendly displayed name
#         """
#         return f"<Phone {self.brand}>"
# class AddressBook:
#     def __init__(self):
#         """
#         A container for Contact objects, representing a Contacts book
#         """
#         self.contacts_list = []
#     def add_contact(self, contact):
#         """
#         Adds a contact to the Address book
#         :param contact: (Contact) contact to add
#         """
#         if not type(contact) == Contact:
#             raise TypeError(f"Can only add Contact objects to AddressBook, not {type(contact)}")
#         self.contacts_list.append(contact)
#     def __call__(self):
#         print("Address book has been executed !")
#     def __add__(self, another_book):
#         """
#         Handling the + operator
#         """
#         new_book = AddressBook()
#         for c in self.contacts_list:
#             new_book.add_contact(c)
#         for c in another_book.contacts_list:
#             new_book.add_contact(c)
#         return new_book
#     def __iadd__(self, another_book):
#         for c in another_book.contacts_list:
#             self.add_contact(c)
#         return self
#     def __str__(self):
#         return f"<Address Book ({len(self.contacts_list)} contacts)>"
#     def __len__(self):
#         return len(self.contacts_list)
# class Contact:
#     def __init__(self, name, phone_nb="", mail="", address=""):
#         """
#         Representing a contact
#         :param name: (str) Name of the contact
#         :param phone_nb: (str) Phone number
#         :param mail: (str) Mail address of the contact
#         :param address: (str) Physical address of the contact
#         """
#         self.name       = name
#         self.phone_nb   = phone_nb
#         self.mail       = mail
#         self.address    = address
#     def __str__(self):
#         return f"<Contact '{self.name}'>"
# johns_book = AddressBook()
# emilys_book = AddressBook()
# johns_contacts = [
#     Contact("Rick Smith", "0586878398", mail="ricksmith@gmail.com"),
#     Contact("Morty Smith", "0585878400", mail="mortysmith@gmail.com"),
#     Contact("Jerry Smith", "0546930747", mail="jerrysmith@gmail.com"),
# ]
# emilys_contacts = [
#     Contact("Homer Simpsons", "0586878398", mail="homersimp@gmail.com"),
#     Contact("Marge Simpsons", "0587113385", mail="margsimp@gmail.com"),
#     Contact("Bart Simpsons", "0587002187", mail="bartsimp@gmail.com"),
# ]
# for c in johns_contacts:
#     johns_book.add_contact(c)
# for c in emilys_contacts:
#     emilys_book.add_contact(c)
# #emilys_book()
# class Robot:
#     def __init__(self, name, set_of_instructions):
#         self.name                   = name
#         self.set_of_instructions    = set_of_instructions
#     def __call__(self):
#         print(f"{self.name} is executing:")
#         for instruction in self.set_of_instructions:
#             print(instruction)
#     def describe(self):
#         print("My name is", self.name)






# robot = Robot("Wall-E",
#               [
#                  "Go to the room",
#                  "Take the dirty clothes",
#                  "Go to the laundry",
#                  "Put the clothes in the wash machine"
#               ]
#         )
# for method in dir(Robot):
#     print(method)






# def numbers_range(a, b, step):
#     """
#     Returns a list of numbers from a to b with a step of steps
#
#     """
#     numbers = []
#     current_number = a
#     while current_number < b:
#         numbers.append(current_number)
#         current_number += step
#
#     return numbers
#
# print(numbers_range(1, 200, 5))

# VS

# def numbers_range(a, b, step):
#     """
#     Returns a list of numbers from a to b with a step of steps
#
#     """
#     numbers = []
#     current_number = a
#     while current_number < b:
#
#         # YIELD the current number (returning it but without stopping the function, then goes to sleep
#         # until python asks for the next one)
#         yield current_number
#         current_number += step
#
# my_numbers_gen = numbers_range(1, 20, 5)
#
# for nb in my_numbers_gen():
#     print(nb)