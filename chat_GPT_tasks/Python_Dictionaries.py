# Perfect! Since you’ve already learned about **Python Sets**, we can now move on to **Dictionaries** — one of the most powerful data structures in Python.
# Here are **3 practical exercises** (in English) to help you practice Python Dictionaries 👇
#
# ---
#
# ### 🧮 **Exercise 1: Student Grades Dictionary**
#
# **Task:**
# Create a dictionary that stores **student names** as keys and their **grades** as values.
# Then:
#
# 1. Print the grade of a specific student.
# 2. Add a new student and grade.
# 3. Update an existing student’s grade.
# 4. Print all student names and grades.
#
# **Example:**
#
# ```python
# students = {
#     "Alice": 90,
#     "Bob": 85,
#     "Charlie": 92
# }
# ```
#
# **Output (example actions):**
#
# ```
# Bob's grade: 85
# Updated students: {'Alice': 90, 'Bob': 88, 'Charlie': 92, 'David': 79}
# ```
#
#================================Task 1 start========================================
# students = {
#     "Alice": 90,
#     "Bob": 85,
#     "Charlie": 92
# }
# print("Bob's grade:", students["Bob"])
# students.update({"Alan": 75, "Bob": 13})
# print("Updated students:", students)
#================================Task 1 end=========================================
#
# ### 🛒 **Exercise 2: Simple Shopping Cart**
#
# **Task:**
# Create a dictionary called `cart` where the keys are **product names** and the values are **prices**.
# Then:
#
# 1. Print the total cost of all items.
# 2. Add a new product.
# 3. Remove one product.
# 4. Print the final cart.
#
# **Example:**
#
# ```python
# cart = {
#     "apple": 2.5,
#     "banana": 1.2,
#     "milk": 3.8
# }
# ```
#
# **Output:**
#
# ```
# Total cost: 7.5
# Cart after adding 'bread': {'apple': 2.5, 'banana': 1.2, 'milk': 3.8, 'bread': 2.0}
# Cart after removing 'banana': {'apple': 2.5, 'milk': 3.8, 'bread': 2.0}
# ```
#
#================================Task 2 start=======================================
# cart = {
#     "apple": 2.5,
#     "banana": 1.2,
#     "milk": 3.8
# }
# print("Total cost:", sum(cart.values()))
# cart.update({"bread": 1.5})
# print("Cart after adding 'bread':", cart)
# cart.pop("banana")
# print("Cart after removing 'banana':", cart)
#================================Task 2 end=========================================
#
# ### 🌍 **Exercise 3: Country Capitals**
#
# **Task:**
# Create a dictionary with **countries** as keys and their **capitals** as values.
# Then:
#
# 1. Ask the user to input a country name.
# 2. Print its capital (if it exists).
# 3. If the country isn’t in the dictionary, print “Country not found”.
#
# **Example:**
#
# ```python
# capitals = {
#     "France": "Paris",
#     "Italy": "Rome",
#     "Germany": "Berlin"
# }
# ```
#
# **Input/Output Example:**
#
# ```
# Enter a country: Italy
# Capital: Rome
# ```
#
# or
#
# ```
# Enter a country: Spain
# Country not found
# ```
#
#================================Task 3 start=======================================
# capitals = {
#     "France": "Paris",
#     "Italy": "Rome",
#     "Germany": "Berlin"
# }
# Country_name = input("Enter a country: ")
# if Country_name in capitals:
#     print("Capital:", capitals.get(Country_name))
# else:
#     print("Country not found")
#================================Task 3 end=========================================
#
# Would you like me to add a **4th “bonus challenge”** that mixes dictionaries with lists (e.g., a list of dictionaries for multiple students or products)?
