# My goal: modify the behaviour of say_hello or say_goodbye so it prints the same thing 3 times (run
# 3 times) BUT without touching the function


# Conditions for a function to be called "Decorator":
# 1) It needs to receive a function AND ONLY A FUNCTION
# 2) It needs to return a function AND ONLY A FUNCTION
# Most of the time, the decorator creates an inner function that wraps the original function

# def triple_exec(function):
#     def inner_function():
#         function()
#         function()
#         function()
#         function()
#         function()
#
#     return inner_function
#
#
# def time_taker(function_2):
#     def second_inner():
#         import time
#         before = time.time()
#         function_2()
#         end = time.time()
#         print(f"Function took {end-before} seconds")
#
#     return second_inner
#
# def run_in_box(func):
#     def function(*args, **kwargs):
#         print("="*50)
#         func(*args, **kwargs)
#         print("=" * 50)
#
#     return function
#
#
# @time_taker
# @run_in_box
# @triple_exec
# def say_hello():
#     print("Hello world !")
#
#
# # say_hello = triple_exec(say_hello)
#
# def say_goodbye():
#     print("Goodbye !")
#
#
# say_hello()
#
#
# @run_in_box
# def say_something(msg):
#     print("You have a message")
#     print(msg)
#
# say_something("Hi, nice to meet you")



# MODULES

# import module_1
#
# module_1.say_hello()

from module_1 import say_good_bye

# say_good_bye()

# import random
#
# import sys
# sys.executable


# import time
#
# print(time.time())

import json

