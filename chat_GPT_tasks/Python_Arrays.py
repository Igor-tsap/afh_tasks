# Here are **3 practical tasks** on **Python Arrays**, using only the topics you have already learned.
# Plain text, easy to copy, no code boxes.
#
# ---
#
# **Task 1: Basic array creation and access**
# Create an array of integers with at least 5 numbers.
# Print:
# • the first element
# • the last element
# • the total number of elements in the array
#
# =====================================Task 1 end=======================================
# int_array = [5, 67, 43, 12, 43, 8, 1, 93, 113, 7, 3]
#
# print(int_array[0])
# print(int_array[-1])
# print(len(int_array))
# =====================================Task 1 end=======================================
#
# **Task 2: Array iteration and condition check**
# Create an array of numbers.
# Use a loop to go through the array and:
# • print each number
# • if the number is greater than 10, also print “greater than 10”
#
# =====================================Task 2 end=======================================
# int_array = [5, 67, 43, 12, 43, 8, 1, 93, 113, 7, 3]
#
# for num in int_array:
#     if num > 10:
#         print(f"{num} is greater than 10")
#     else:
#         print(num)
# =====================================Task 2 end=======================================
#
# **Task 3: Modify array values**
# Create an array of numbers.
# Ask the user for a number to add to the array.
# Add the number to the array.
# Then use a loop to calculate and print the sum of all numbers in the array.
#
# =====================================Task 3 end=======================================
# int_array = [5, 67, 43, 12, 43, 8, 1, 93, 113, 7, 3]
#
# add_num = int(input("add number: "))
#
# int_array.append(add_num)
#
# the_sum = 0
# for num in int_array:
#     the_sum += num
#     print(the_sum)
#
# print(the_sum)
# =====================================Task 3 end=======================================
#
# If you want, I can also give you a **challenge version** mixing arrays with try/except or functions.



