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
# Task 4 — Safe dictionary lookup
# Create a dictionary with 3 products and their prices.
# Ask the user to enter a product name.
# Use try/except to catch a KeyError when the product does not exist.
# If the product is found, print its price.
# If not, print “Product not found”.
# =====================================Task 4 start=====================================
# my_dict = {
#     "milk": 40,
#     "bread": 30,
#     "eggs": 90
# }
#
# user_search = input("enter product: ")
#
# try:
#     print(my_dict[user_search])
# except KeyError:
#     print("Product not found")
# =====================================Task 4 end=======================================
# Task 5 — Safe list-to-int conversion
# Create a list containing strings: ["10", "20", "hello", "30"].
# Ask the user for an index.
# Use try/except to catch:
# • IndexError (invalid index)
# • ValueError (when converting item to int fails)
# If successful, convert the item to int and multiply it by 3.
# If an error occurs, print the correct message.
# =====================================Task 5 start=====================================
# my_list = ["10", "20", "hello", "30"]
#
# try:
#     user_index = int(input("enter index: "))
#     print(int(my_list[user_index]) * 3)
#
# except IndexError:
#     print("invalid index")
#
# except ValueError:
#     print("invalid number")
# =====================================Task 5 end=======================================
# Task 6 — Repeating input until valid
# Ask the user to enter a valid number between 1 and 5.
# Use a while loop + try/except:
# • Try to convert input to int
# • If ValueError happens, print “Not a number”
# • If number is out of range, print “Number out of range”
# Keep asking until the user enters a correct number.
# When they finally enter it, print “Thank you!”
# =====================================Task 6 start=====================================
# # while True:
# #     user_number = input("enter number 1-5: ")
# #
# #     try:
# #         if not 1 <= int(user_number) <= 5:
# #             raise Exception
# #     except ValueError:
# #         print("Not a number")
# #     except Exception:
# #         print("Number out of range")
# #     else:
# #         print("Thank you!")
# #         break
#
# while True:
#     try:
#         number = int(input("enter number 1-5: "))
#
#         if 1 <= number <= 5:
#             print("Thank you!")
#             break
#         else:
#             print("Number out of range")
#
#     except ValueError:
#         print("Not a number")
# =====================================Task 6 end=======================================
# Task 7 — Safe division
#
# Ask the user for two numbers.
# Use try/except to catch invalid input (ValueError) and division by zero (ZeroDivisionError).
# If both numbers are valid and division is possible, print the result.
# =====================================Task 7 start=====================================
# try:
#     num1 = int(input("num1: "))
#     num2 = int(input("num2: "))
#     print(num1 / num2)
#
# except ValueError:
#     print("invalid number")
#
# except ZeroDivisionError:
#     print("division by zero")
# =====================================Task 7 end=======================================
# Task 8 — List sum with user indices
#
# Create a list of 5 numbers.
# Ask the user for two indices.
# Use try/except to handle:
# • IndexError if an index is out of range
# • ValueError if the input is not a number
# If both indices are valid, print the sum of the two list items.
# =====================================Task 8 start=====================================
# my_list = [5, 8, 23, 65, 5]
# try:
#     user_index1 = int(input("enter num1 0-4: "))
#     user_index2 = int(input("enter num2 0-4: "))
#     # print(sum([my_list[user_index1], my_list[user_index2]]))
#     print(my_list[user_index1] + my_list[user_index2])
#
# except IndexError:
#     print("index is out of range")
#
# except ValueError:
#     print("not a number")
# =====================================Task 8 end=======================================
# Task 9 — Dictionary key check
#
# Create a dictionary with 3 students and their ages.
# Ask the user to enter a student name.
# Use try/except to catch KeyError if the name doesn’t exist.
# If the name exists, print the student’s age.
# =====================================Task 9 start=====================================
# students = {
#     "bob": 13,
#     "tom": 26,
#     "tim": 41
# }
#
# try:
#     user_name = input("name: ")
#     print(students[user_name])
#
# except KeyError:
#     print("name doesn’t exists")
# =====================================Task 9 end=======================================
# Task 10 — Math operations with input
#
# Ask the user to enter a number.
# Use try/except to catch invalid input (ValueError).
# If valid, calculate:
# • square using ** operator
# • square root using math.sqrt()
# Print both results.
# =====================================Task 10 start=====================================
# from math import sqrt
#
# try:
#     user_num = int(input("enter num: "))
#
# except ValueError:
#     print("invalid input")
#
# else:
#     print(user_num ** 2)
#     print(sqrt(user_num))
# =====================================Task 10 end=======================================