# Here are 3 practical tasks for **Python For Loops**, based only on the topics you have already learned:
#
# 1. Create a list of 5 different numbers. Use a for loop to calculate and print the sum of all numbers in the list.
#================================Task 1 start========================================
# my_list = [1, 7, 8, 4, 3]
# the_sum = 0
# for number in my_list:
#     the_sum += number
# print(the_sum)
#================================Task 1 end==========================================
# 2. Create a string with any sentence you like. Use a for loop to count how many times the letter "a" appears in the string. Print the final count.
#================================Task 2 start========================================
# the_string = "Срака горіла, маку не їла"
#
# count = 0
#
# for letter in the_string:
#     if letter == "а":
#         count += 1
#
# print(count)
#================================Task 2 end==========================================
# 3. Create a dictionary with 3 key-value pairs (for example, product names and prices). Use a for loop to print each key and its value in the format: "key: value".
#================================Task 3 start========================================
# my_dict = {
#     "bread" : 30,
#     "cheese" : 120,
#     "eggs" : 100
# }
#
# for item in my_dict:
#     print(f"{item}: {my_dict[item]}")
#================================Task 3 end==========================================
# Here are 3 practical tasks for Python For Loops, based on everything you have learned so far:
#
# Create a function that takes a list of numbers as a parameter. Use a for loop and the range() function to print each number multiplied by 2.
#================================Task 4 start========================================
# def multiplier_by_2(*my_list):
#     for item in my_list:
#         print(item * 2)
#
# multiplier_by_2(1, 2, 3, 6, 3)

#================================Task 4 end==========================================
# Create an array with 5 items (any strings). Use a for loop with an iterator to go through the array and print each element in uppercase.
#================================Task 5 start========================================
# my_array = ["dog", "cat", "parrot", "cow", "Angela Merkel"]
# for index in range(len(my_array)):
#     print(my_array[index].upper())
#================================Task 5 end==========================================
# Create a module (a separate .py file) that contains a function returning today’s date.
# In your main script, import this module and use a for loop to print the date 7 times.
#================================Task 6 start========================================
# import module
#
# for index in range(7):
#     print(module.todays_date())
#================================Task 6 end==========================================