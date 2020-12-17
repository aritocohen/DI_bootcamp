# """
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# """
#
#
# class Zoo():
#
#     def __init__(self, zoo_name):
#         self.name = zoo_name
#         self.animals = []
#
#     def add_animal(self, new_animal):
#         """
#         Add animal to the zoo only if the animal is not already in the list
#         """
#
#         # To avoid string comparaison problems, set every animal to lowercase
#         new_animal = new_animal.lower()
#
#         # Check if the animal is already in the list
#         if new_animal in self.animals:
#             return False
#
#         # Don't need the else here, because the function will be stopped if new_animal is in self.animals
#
#         # Add the animal to the list of animals
#         self.animals.append(new_animal)
#
#     def sell_animal(self, animal_sold):
#         """
#         Sells an animal, remove it from the list
#         :param animal_sold: (str) animal to sell
#         """
#         # Check if the animal is in the list
#         if animal_sold in self.animals:
#             # If it is, remove it from the list
#             self.animals.remove(animal_sold)
#
#     def print_animals(self):
#         """
#         Prints the list of the animals in the zoo
#         """
#         # Make a for loop on every animal
#         for animal in self.animals:
#             print(f"- {animal.title()}")
#
#     def sort_animals(self):
#         """
#         Returns a dictionary where each key is the index of the animal name sorted alphabetically and its value is
#         the list of all the animals starting with the same letter
#         For example ["Ape", "Babcoon", "Bear" ... "Eel", "Emu"] will return:
#         {
#             1: "Ape",
#             2: ["Baboon", "Bear"],
#             3: ['Cat', 'Cougar'],
#             4: ['Eel', 'Emu']
#         }
#         """
#         sorted_animals = sorted(self.animals)  # Function that receives a list and returns a sorted list
#         animals_index = {}
#         current_letter = ""
#
#         # 1) Take every animal in the sorted list
#         #      1.1) Create the list of all the animals that starts with the same letter
#         #      1.2) Add this list to the dictionary
#         #      1.3) Ignore every animal that starts with the same letter
#
#         letter_index = 1
#
#         for animal in sorted_animals:
#
#             # Check if this letter hasn't been checked already
#             if animal[0] == current_letter:
#                 continue  # Skip this iteration
#
#             # Create a list of all the animals that start with the same letter
#             same_letter = []
#             for animal_2 in sorted_animals:
#                 # Compare the two first letters
#                 if animal[0] == animal_2[0]:
#                     # If they are the same, add this animal to the list of the animals with the same letter
#                     same_letter.append(animal_2)
#
#             animals_index[letter_index] = same_letter
#             letter_index += 1
#
#             # Set current letter to the first letter of the animal
#             current_letter = animal[0]
#
#         return animals_index
#
#     def print_groups(self):
#         # Retrieve the groups
#         groups = self.sort_animals()
#         for animals in groups.values():
#
#             # Print the animals one by one
#             for animal in animals:
#                 print("-", animal.title())
#
#             # Print a line of =
#             print("=" * 10)
#
#
# ramat_gan_safari = Zoo("Ramat Gan Safari")
#
#


# class Circle:
#     color = "red"
#
# class NewCircle(Circle):
#     color = "blue"
#
# nc = NewCircle
# print(nc.color)

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter
#
#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor
#
# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)
#
# nc = NewCircle(1)
# print(nc.diameter)
# nc.grow()
# print(nc.diameter)