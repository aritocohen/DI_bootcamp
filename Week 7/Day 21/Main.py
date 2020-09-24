# my_number = '1234'
# my_list = []
#
# for num in my_number:
#     my_list.append(num)
# print(my_list)




# for item in enumerate("abdc"):
#     print(item)

# for i in range(1, 1000):
#     print(i)
# else:
#     print('The for loop is over')




# x = 0
#
# while x < 1000:
#     print(f' x is {x}')
#     x+= 1
# else:
#     print('We have reached 1000')


# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='')  # end='' renders each letter next to the other
#


# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')


# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print('Input is of sufficient length')


# EX XP day 19

# Ex1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# my_dict = dict(zip(['Ten', 'Twenty', 'Thirty'],[10, 20, 30]))
#
# print(my_dict)

# Ex2

# store = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": 'Amancio Ortega Gaona',
#     "type_of_clothes": ['men', 'women', 'children', 'home'],
#     "international_competitors": ["Gap", "H & M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": ['France -> blue', 'Spain -> red', 'US -> pink, green']
# }

# store['number_stores'] = 2

# print("Zara main clientes are ", store["type_of_clothes"])

# store["country_creation"] = "Spain"

# store["international_competitors"] = [store["international_competitors"], "Desigual"]

# del store["creation_date"]

# print(store["international_competitors"][-1])

# print('The major clothes color in the', store["major_color"][-1])

# print(len(store))

# print(store.keys())


# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
#
# store.update(more_on_zara)
#
# print(store["number_stores"])

# Ex3

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
#
# for item in enumerate(users):
#     print(item)


