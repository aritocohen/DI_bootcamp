# OOP

# class Dog():
#     def __init__(self, age, name, breed):
#         print("A new dog is being created")
#         self.age    = age
#         self.name   = name
#         self.breed  = breed
#         self.energy_level = 100
#         self.run_count = 0
#
#     def bark(self):
#         print(f"{self.name} is Barking ! WOOF")
#
#     def eat(self):
#         print(f"{self.name} is eating")
#         self.energy_level += 30
#
#     def run(self):
#         if self.energy_level < 40:
#             print(f"{self.name} is tired, cannot run at the moment")
#         else:
#             print(f"{self.name} is running!")
#             self.energy_level -= 15
#             self.run_count += 3
#
#     def describe(self):
#         print(f"Dog {self.name}: {self.age} years old {self.breed}")
#         print(f"Energy: {self.energy_level}/100")
#         print(f"Traveled: {self.run_count} km")
#
# my_dog  = Dog(10, "Uma", "Chow chow")
# my_dog2 = Dog(14, "Wanda", "adopted")
#
# Dog.bark(my_dog)
# it is the same as:
# my_dog.run()
# my_dog.run()
# my_dog.run()
# my_dog.run()
# my_dog.eat()
# my_dog.eat()
# my_dog.run()
# my_dog.run()
#
# my_dog2.run()
# my_dog2.run()
# my_dog2.run()
#
# my_dog.describe()
# my_dog2.describe()


# excersice


class Spell():
    def __init__(self, name, invocation, action, min_level):
        print("You are about to learn a spell")
        self.name = name
        self.invocation = invocation
        self.action = action
        self.min_level = min_level


spell_one = Spell("The opening one", "Alohomora", "Open locks", 3)
spell_two = Spell("The lifting one", "Vinguardion leviousa", "lift objects in the air", 5)
spell_list = []

spell_list.append(spell_one)
spell_list.append(spell_two)


class SpellsBook():
    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def remove_spell(self, spell):
        self.spells.remove(spell)

    def use_spell(self, spell_name):
        for spell in self.spells:
            if spell.name == spell_name:
                print(spell.invocation)
                print(spell.action)

    def describe(self):
        print("Here are the spells I learned:")
        for spell in self.spells:
            print(f"{spell.name}")


spell_book = SpellsBook()
spell_book.add_spell(spell_one)
spell_book.add_spell(spell_two)

spell_book.describe()


# SpellsBook(spell_two)


class Wizzard():
    def __init__(self, name, w_name,):
        self.name = name
        self.w_name = w_name

        self.level = 1
        self.book = SpellsBook()
        self.xp = 0

    def learn_spell(self, spell):
        if self.level >= spell.min_level:
            self.book.add_spell(spell)
        else:
            print("Sorry, you cannot learn this spell yet")

    def check_level(self):


    def use_spell(selfself, spell_name):
        self.book.use_spell(spell_name)
        self.xp += 25
        if self.xp >= 100:
            self.level += 1
            self.xp = 0


wizzard_1 = Wizzard("Gandalf", "The grey")
wizzard_2 = Wizzard("Saruman", "The white")
wizzard_list = []

wizzard_list.append(wizzard_1)
wizzard_list.append(wizzard_2)


