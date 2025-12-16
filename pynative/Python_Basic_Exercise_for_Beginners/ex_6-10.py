# Exercise 6: Display numbers divisible by 5
#
# Write a Python code to display numbers from a list divisible by 5
#
# Expected Output:
#
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55
# =====================================ex_6_start=====================================
# my_list1 = [10, 20, 33, 46, 55]
#
# # # new_list = list(filter(lambda n: n % 5 == 0, my_list1))
# # #
# # # for num in new_list:
# # #     print(num)
# #
# # for num in my_list1:
# #     if num % 5 == 0:
# #         print(num)
#
# new_list = [num for num in my_list1 if num % 5 == 0]
#
# for num in new_list:
#     print(num)
# =====================================ex_6_end=======================================
# Exercise 7: Find the number of occurrences of a substring in a string
#
# Write a Python code to find how often the substring “Emma” appears in the given string.
#
# Given:
#
# str_x = "Emma is good developer. Emma is a writer"
# =====================================ex_7_start=====================================
# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma"))
# =====================================ex_7_end=======================================
# Exercise 8: Print the following pattern
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# =====================================ex_8_start=====================================
# for num in range(1, 6):
#     print(f"{num} " * num)
#
# # for num in range(6):
# #     for times in range(num):
# #         print(num, end=" ")
# #     print("")
# =====================================ex_8_end=======================================
# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome number
# =====================================ex_9_start=====================================
# original_number = input("enter num: ")
# reversed_number = original_number[::-1]
#
# if original_number == reversed_number:
#     print("Yes. given number is palindrome number")
# else:
#     print("No. given number is not palindrome number")
# =====================================ex_9_end=======================================
# Given two lists of numbers, write Python code
# to create a new list containing odd numbers from the first list and even numbers from the second list.
#
# Given:
#
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
#
# Expected Output:
#
# result list: [25, 35, 40, 60, 90]
# =====================================ex_10_start====================================
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
#
# list3 = [num for num in list1 if num % 2 == 1]
# list4 = [num for num in list2 if num % 2 == 0]
# 
# print(f"result list: {list3 + list4}")
# =====================================ex_10_end======================================