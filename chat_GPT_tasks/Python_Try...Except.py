# Here are 3 practical tasks on **Python Try...Except**, in simple English and easy to copy:
# 1. Create a function that asks the user to enter a number. Use try/except to catch an error if the user types text instead of a number.
# If an error happens, print a message like “Invalid input”. If everything is correct, print the number multiplied by 5.
# =====================================Task 1 start=====================================
# def user_number():
#     return int(input("Enter a number: "))
#
# try:
#     my_number = user_number()
# except:
#     print("Invalid input")
# else:
#     print(my_number * 2)
# =====================================Task 1 end=======================================
# 2. Create a list with a few numbers. Ask the user for an index number.
# Use try/except to catch an IndexError if the user enters an index that does not exist in the list.
# If the index is valid, print the element. If not, print “Index out of range”.
# =====================================Task 2 start=====================================
# my_list = [15, 6, 12, 67, 43, 87, 23, 7, 8, 5]
#
# user_index = int(input("Enter a number 0-9: "))
#
# try:
#     my_number = my_list[user_index]
# except:
#     print("Index out of range")
# else:
#     print(my_number)
# =====================================Task 2 end=======================================
# Task 3 — Math operation with error handling
#
# Ask the user for two numbers.
# Ask what operation they want: “add”, “subtract”, “multiply”, or “divide”.
# Use try/except to handle:
# • invalid number
# • division by zero
#
# (Hints: input, casting, if/else, arithmetic operators, except ZeroDivisionError.)
# =====================================Task 3 start=====================================
# result = None
#
# try:
#     number1 = int(input("Enter number 1: "))
#     number2 = int(input("Enter number 2: "))
#     try:
#         operator = input("Enter operation: add, subtract, multiply, or divide: ")
#
#         if operator == "add":
#             result = number1 + number2
#         elif operator == "subtract":
#             result = number1 - number2
#         elif operator == "multiply":
#             result = number1 * number2
#         elif operator == "divide":
#             if number2 != 0:
#                 result = number1 / number2
#             else:
#                 raise ZeroDivisionError
#         else:
#             raise Exception
#     except ZeroDivisionError:
#         print("division by zero")
#     except:
#         print("invalid operator")
# except:
#         print("invalid number")
# else:
#     if result != None:
#         print(result)
# =====================================Task 3 end=======================================
# If you want, I can also make harder tasks or mix multiple topics you already learned.
