# DAY 17


# def get_numb(min_numb, max_numb):
#
#     valid_numb = False
#
#     while not valid_numb:
#         numb: input("Tell me a number")
#         numb: int(numb)
#
#         if min_numb <= numb >= max_numb:
#             valid_numb = True
#         else:
#             print("Invalid number")
#
#     return numb
#
# user_numb = get_numb(0, 20)
# print(user_numb)



# def make_shirt(sentence, size):
#
#     print(f"I created a shirt in size {size} with '{sentence}' written on it")
#
# make_shirt("Hello world", "M")

# def is_upper(s):
#     for char in s:
#         if char != char.upper():
#             return False
#
#     return True


# def happy_birthday(name, age, cake, language="EN"):
#     if language == "EN":
#         print(f'Happy birthdat {name}')
#         print("Here is your cake:")
#
#     elif language == "ES":
#         print(f"Feliz cumple {name}")
#         print("Aca esta tu torta:")
#
#     else:
#         print(f"language {language} is not valid")
#
#     print(cake)
#
# my_cake = ""
# happy_birthday("Ariel", 30, my_cake, "ES")



# def minmax(nbs):
#     return [min(nbs), max(nbs)]
#
# numbers = [1, 234, 5, 65, 123, 43, 765, 12, 1]
# values = minmax(numbers)
# print(values)


# def double_list(original_numbs):
#     nbs = original_numbs.copy()
#     i = 0
#     while i < len(nbs):
#         nbs[i] = nbs[i] * 2
#         i += 1
#
#     return nbs
#
# numbers = [1, 234, 5, 65, 123, 43, 765, 12, 1]
# double_numbers = double_list(numbers)
#
# print(numbers)
# print(double_numbers)






