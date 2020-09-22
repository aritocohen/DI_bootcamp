# my_family = {
#     "father": "Aron",
#     "mother": "Patricia",
#     "children": ["Jeko", "Gabi", "Ariel"]
# }

# sun_flower = {
#     "name": "sun flower",
#     "height": 10,
#     "petals": 19,
#     "color": "yellow",
#     "thorns": False
# }
#
# rose = {
#     "name": "Rose",
#     "height": 5,
#     "petals": 12,
#     "color": "Red",
#     "thorns": True
# }

# my_flowers = [sun_flower, rose]

# i=1
# print("My favorite flowers are:")
# for flower in my_flowers:
#     print(f"{i}) the {flower['name']}, it is {flower['height']} cm high")
#     i += 1

# print(sun_flower["color"])

# access data
# print(f"{sun_flower['name']} is {sun_flower['height']}")

# modify data
# sun_flower["color"] = "red"

# delete key in dictonary
# del rose["height"]

# for item in rose:
#     print(item)

# for keys in rose.keys():
#     print(keys, "--->", rose[keys])

# for values in rose.values():
#     print(values)

# UNPACKING
# family_boys = ["Aron", "Hanania", "Ariel"]
# family_girls = ["Patricia", "Fanny", "jeko"]
# father, granfather, son = family_boys
# print(son)


# sun_flower = {
#     "name": "sun flower",
#     "height": 10,
#     "petals": 19,
#     "color": "yellow",
#     "thorns": False
# }
#
# rose = {
#     "name": "Rose",
#     "height": 5,
#     "petals": 12,
#     "color": "Red",
#     "thorns": True
# }
#
# for i, flower in enumerate(rose):
#     print(f"{i}) {flower}")


# products = {
#     "Computer": 1000,
#     "Iphone": 2000,
#     "Apple wheels": 5000,
#     "PS5": 600,
# }
#
# user_money = int(input("How much money do you have?"))
#
# print("You can afford: ")
#
# for product, price in products.items():
#     if price <= user_money:
#         print(f"~ {products} (${price})")


