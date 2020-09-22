# Lists

# my_list = [1,2,3]

# my_family_members = ["Aaron", "Patricia", "Jeko", "Gabi", "Ariel"]

# my_favorite_letters_and_numbers = ["a", 2, "letter b", 500]

# print(my_family_members[0:2])

# like the string

# print(len(my_family_members))

# my_family_members.append("Liz")

# print(my_family_members)
#
# my_family_members.remove("Aaron")
#
# my_family_members.pop(3) # Removes the item numb 3
#
# print(my_family_members)
from typing import List

# Ex 1
# user_toppings = []
#
# choice = input("Please choose your pizza toppings (type 'STOP' to stop)")
#
# user_toppings.append(choice)
#
# # Loop
# while choice != "STOP":
#     choice = input("What other topping would you like?")
#
#     if choice != "STOP":
#         user_toppings.append(choice)
#
# print(user_toppings)

# Ex 2



# user_attempts = 0
#
# while user_attempts < 4:
#
#     user_pass = input("Please type your password")
#
#     if len(user_pass) < 6:
#         print("Your password is too short")
#
#     if len(user_pass) > 12:
#         print("Your password is too long")
#
#     user_attempts = user_attempts + 1


# my_family = ["Ari", "Aaron", "Patricia", "Jeko", "Gabi"]
#
# for member in my_family:
#     age_member = input("How old are you,"member)
#     age_member = int age_member
#
#     if age_member < 16:
#         my_family.remove((member))



# XP CHALLENGE

# EX 1
# my_fav_numbers = [1, 3, 7, 9]
#
# my_fav_numbers.append(5)
# my_fav_numbers.append(2)
#
# my_fav_numbers.pop()
#
# friend_fav_numbers = [12, 14, 22]
#
# my_fav_numbers.extend(friend_fav_numbers)
#
# print(my_fav_numbers)

# EX 2

# my_fav_numbers = (1, 3, 7, 9)
#
# my_fav_numbers.append(5)
# my_fav_numbers.append(2)
#
# my_fav_numbers.pop()
#
# friend_fav_numbers = (12, 14, 22)
#
# my_fav_numbers.extend(friend_fav_numbers)
#
# print(my_fav_numbers)

#Ex 3

# list_with_floats = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
#
# print(list_with_floats)

my_age = 29
my_age_in = my_age + 123879
print(my_age_in)
