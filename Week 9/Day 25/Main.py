# Class Attributes

# class Phone():
#
#     spanish_name = 'telefono'
#     objs_count = 0
#
#     def __init__(self, brand, size, adapter_type):
#         self.brand          = brand
#         self.size           = size
#         self.adapter_type   = adapter_type
#
#         self.contacts       = []
#
#         Phone.objs_count += 1
#         if Phone.objs_count % 100 == 0:
#             Phone.anniversary()
#
#     @classmethod # Class method
#     def anniversary(cls):
#         print(f"Happy birthdar to the Phone class!! {cls.objs_count} phones have been created so far")
#
#
# my_phone = Phone("Apple", 11, "apple adapter")
#
# Phone.anniversary()


# class Animal():
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name} is eating')
#
#     def drink(self):
#         print(f'{self.name} is drinking')
#
#     def sleep(self):
#         print(f'{self.name} is sleeping')
#
#
# class Reptile(Animal):
#     def drag(self):
#         print(f'{self.name} is dragging')
#
#
# class Mammal(Animal):
#     def walk(self):
#         print(f'{self.name} is walking')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print(f'{self.name} is barking')
#
#
# class Cow(Mammal):
#     def moo(self):
#         print(f'{self.name} is mooing')
#
#
# class Snake(Reptile):
#     def asphyxiate(self):
#         print(f'{self.name} is asphyxiating his dam')
#
# cow = Cow("Milka")
#
# cow.drink()


# excersice


class Hero():
    def __init__(self, name):
        """
        Hero class representing a warrior character
        :param name: (str) Name of the character
        """
        self.name = name
        self.level                  = 1
        self.max_energy             = 100
        self.max_life_points        = 100
        self.hit_dammage            = 10
        self.xp                     = 0
        self.is_alive               = True
        self.current_energy         = self.max_energy
        self.current_life_points    = self.max_life_points
    def hit(self, other_hero):
        """
        Hits another hero
        :param hero: (Hero) Hero to hit
        """
        other_hero.takes_hit(self.hit_dammage)
    def get_xp(self, xp_amount):
        """
        Increase XP points
        Level up if the XP reaches 100
        :param xp_amount: (int) Amount of xp to add
        """
        self.xp += xp_amount
        if self.xp >= 100:
            self.level_up()
    def takes_hit(self, dammage):
        """
        Taking dammage
        Kills the hero if current_life_points goes below 0
        :param dammage: (int) Dammage amount to take
        """
        self.current_life_points -= dammage
        if self.current_life_points <= 0:
            self.die()
    def die(self):
        """
        Kills the hero
        """
        self.is_alive = False
    def level_up(self):
        """
        Levels up the hero
        Add 2 to max_life_points
        Give him all his life points back
        Increment level and set xp back to 0
        """
        self.max_life_points += 2
        self.current_life_points = self.max_life_points
        self.level += 1
        self.xp = 0
