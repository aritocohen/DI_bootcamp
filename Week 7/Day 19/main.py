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

# Ex 2
contacts = {
    "Alpha": "053050505",
    "Beta": "054305305",
    "Romeo": "434535433",
}

contacts["Zulu"] = "123214564"

for name, phone_nb in contacts.items():
    print(f"{name}\t-> {phone_nb}")

searched_name = "alpha"

for name in contacts.keys():
    if name.lower() == searched_name.lower():
        print(f"{name} exists in the contacts")

searched_numb = "123214564"

for name, numb in contacts.items():
    if numb == searched_numb:
        print(f"{searched_numb} belongs to {name}")

aro_contacts = {
    "Charlie": "8453423423",
    "Pepe": "324328654",
}

for name, numb in aro_contacts.items():
    contacts[name] = numb

nb_of_contacts = len(contacts.keys())
print(f"There Are {nb_of_contacts} contacts")

sorted_contacts = sorted(contacts.keys())
for contacts in sorted_contacts:
    print(f"{contacts}\t-> {contacts[contacts]}")
