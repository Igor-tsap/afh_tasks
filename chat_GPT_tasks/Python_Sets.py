
# ### 🧩 **Exercise 1: Unique Words from a Sentence**
#
# **Task:**
# Write a Python program that takes a sentence from the user and prints out all **unique words** using a set.
#
# **Example:**
#
# ```python
# Input: "apple banana apple orange banana"
# Output: {'apple', 'banana', 'orange'}
# ```
#
# **Hint:**
# Use `.split()` to get words and `set()` to remove duplicates.
#
#================================Task 1 start=======================================
# my_info = input("give me list of fruits: ")
# my_list = my_info.split()
# print(set(my_list))
#================================Task 1 end=========================================
#
# ### ⚙️ **Exercise 2: Common and Different Items**
#
# **Task:**
# Create two sets:
#
# * one for fruits you like
# * one for fruits your friend likes
#
# Then print:
#
# 1. The fruits you both like (intersection)
# 2. The fruits only you like (difference)
# 3. All fruits either of you like (union)
#
# **Example:**
#
# ```python
# my_fruits = {"apple", "banana", "cherry"}
# friend_fruits = {"banana", "kiwi", "cherry"}
# ```
#
# **Output:**
#
# ```
# Both like: {'banana', 'cherry'}
# Only I like: {'apple'}
# All fruits: {'apple', 'banana', 'cherry', 'kiwi'}
# ```
#
#================================Task 2 start=======================================
# my_fruits = {"apple", "pear", "hazelnuts"}
# wife_fruits = {"mango", "avocado", "hazelnuts"}
# print("Both like:",  my_fruits & wife_fruits)
# print( "Only I like:", my_fruits - wife_fruits)
# print("All fruits:", my_fruits | wife_fruits)
#================================Task 2 end=========================================
#
# ### 🔄 **Exercise 3: Removing Duplicates from a List**
#
# **Task:**
# You have a list with repeated numbers.
# Use a set to remove duplicates and print both the original list and the cleaned one.
#
# **Example:**
#
# ```python
# numbers = [1, 2, 3, 2, 4, 1, 5]
# ```
#
# **Output:**
#
# ```
# Original list: [1, 2, 3, 2, 4, 1, 5]
# Without duplicates: [1, 2, 3, 4, 5]
# ```
#
# **Hint:**
# Convert the list to a set and back to a list again.
#
#================================Task 3 start=======================================
# numbers = [1, 2, 3, 2, 4, 1, 5]
# my_set = set(numbers)
# print("Original list:", numbers)
# print("Without duplicates:", list(my_set))
#================================Task 3 end=========================================