# Below are three practical tasks focused on Python Iterators. They are written in plain English, easy to copy,
# and assume knowledge of the topics you have already completed (lists, loops, functions, range, etc.).

# Task 1: Manual iteration with iter() and next()
# Create a list of at least five items (for example: names, numbers, or cities).
# Convert this list into an iterator using iter().
# Use next() multiple times to manually retrieve and print each element one by one.
# After the iterator is exhausted, observe and explain what happens when next() is called again.

# =====================================Task 1 start=====================================
# int_array = [5, 67, 43, 12, 43, 8, 1, 93, 113, 7, 3]
#
# my_it = iter(int_array)
#
# try:
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#     print(next(my_it))
#
# except StopIteration:
#     print("end of the array")
# =====================================Task 1 end=======================================

# Task 2: Custom iterator using a class
# Create a custom iterator class that iterates over numbers from 1 to a given limit.
# The limit should be passed when creating the object.
# Use a for loop to iterate over an instance of this class and print each value.
# Add a short comment explaining the role of iter() and next() in your own words.

# =====================================Task 2 start=====================================
# class Iterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= self.limit:
#             next_num = self.num
#             self.num += 1
#             return next_num
#
#         else:
#             raise StopIteration
#
# my_it = iter(Iterator(7)) #iter() converts object (iterable) to iterator
#
# print(next(my_it)) # next() returns next index of iterator
# print(next(my_it))
# print(next(my_it))
# print(next(my_it))
#
# print("-" * 50)
#
# for num in my_it: #for loop continues from the next index, not from the beginning
#     print(num)
#
# print("-" * 50)
#
# for num in Iterator(5):
#     print(num)
#


# =====================================Task 2 end=======================================

# Task 3: Iterator vs iterable comparison
# Create a list of strings and loop over it twice using two separate for loops.
# Then convert the same list into an iterator and try to loop over it twice.
# Compare the results and write a short explanation of why the behavior is different.
# In your explanation, clearly distinguish between an iterable and an iterator.

# =====================================Task 3 start=====================================
# my_list = ["apple", "banana", "coconut", "cherry", "carrot"]
#
# for string in my_list:
#     print(string)
#
# for string in my_list:
#         print(string)
#
# print("-" * 50)
#
# my_it = iter(my_list)
# # iterator variable can be iterated only once.
# # it is also visible in task 2 - where I made for loop after manual next()s - and it continued iteration at next index, not from the beginning
#
# for string in my_it:
#     print(string)
#
# for string in my_it:
#     print(string)
#
# for string in my_it:
#     print(string)

# =====================================Task 3 end=======================================