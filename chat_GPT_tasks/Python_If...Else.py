# Perfect 👍 Since you’ve already covered up to **Python Dictionaries**, you’re ready for some good practical exercises with **if...else** that use what you’ve learned so far.
#
# Here are **3 practical Python exercises on “If…Else”** — in English and matched to your current level:
#
# ---
#
# ### 🧩 **Exercise 1: Even or Odd**
#
# **Task:**
# Ask the user to enter a number.
# Use an **if...else** statement to check if the number is **even** or **odd**, and print the result.
#
# **Example:**
#
# ```python
# Input: 7
# Output: 7 is an odd number.
# ```
#
# **Hint:**
# Use the modulus operator `%` to check the remainder when dividing by 2.
#
#================================Task 1 start========================================
# number = input("Enter a number: ")
# if int(number) % 2 == 1:
#     print(number, "is an odd number")
# else:
#     print(number, "is an even number")
#================================Task 1 end==========================================
#
# ### 🍎 **Exercise 2: Grade Checker**
#
# **Task:**
# Ask the user to enter their test score (0–100).
# Using **if...elif...else**, print the grade based on this scale:
#
# * 90–100 → A
# * 80–89 → B
# * 70–79 → C
# * 60–69 → D
# * Below 60 → F
#
# **Example:**
#
# ```python
# Input: 85
# Output: Your grade is B.
# ```
#
# **Hint:**
# Use multiple `elif` conditions to check score ranges.
#
#================================Task 2 start========================================
# grade = input("Enter your grade: ")
# if int(grade) >= 90:
#     print("Your grade is A")
# elif int(grade) >= 80:
#     print("Your grade is B")
# elif int(grade) >= 70:
#     print("Your grade is C")
# elif int(grade) >= 60:
#     print("Your grade is D")
# else:
#     print("Your grade is F")
#================================Task 2 end==========================================
#
# ### 🛒 **Exercise 3: Discount Calculator**
#
# **Task:**
# Create a program that asks the user for the total price of their shopping.
# If the total is **over 100**, apply a **10% discount**.
# Otherwise, print that there is **no discount**.
#
# **Example:**
#
# ```python
# Input: 120
# Output: You get a 10% discount! Final price: 108.0
# ```
#
# **Hint:**
# You can use simple math like `price * 0.9` to apply the discount.
#
#================================Task 3 start========================================
# total_price = input("Enter the total price of your shopping: ")
# if int(total_price) >= 100:
#     print("You get a 10% discount! Final price: ", (int(total_price) * 0.9))
# else:
#     print("No discount :(")
#================================Task 3 end==========================================
#
# Would you like me to make a **“challenge version”** of these tasks — combining **if...else** with **lists** or **dictionaries** (like checking if an item is in stock)?
