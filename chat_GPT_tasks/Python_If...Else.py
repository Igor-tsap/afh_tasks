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
# Challenge 1: Inventory Checker
#
# Create a dictionary that stores items and their stock count, for example:
# • "apple": 10
# • "banana": 0
# • "orange": 5
#
# Ask the user to enter an item name.
# Use if…else to check:
#
# If the item exists in the dictionary → print the stock count
#
# If the stock count is 0 → print “Out of stock”
#
# If the item does not exist → print “Item not found”
#================================Task 4 start========================================
# item_count = {
#     "apple": 10,
#     "banana": 0,
#     "orange": 5
#     }
# fruit_search = input("Enter a fruit: ")
# if fruit_search in item_count:
#     if item_count[fruit_search] == 0:
#         print("Out of stock")
#     else:
#         print(item_count[fruit_search])
# else:
#     print("Item not found")
#================================Task 4 end==========================================
#
# Challenge 2: Shopping List Verifier
#
# Create a list of items that a user wants to buy (for example: “milk”, “bread”, “eggs”).
# Also create a dictionary of prices for items.
#
# Ask the user to type an item name.
# Use if…else to check:
#
# If the item is in the shopping list → print “This item is on your list”
#
# If it's not on the list but exists in the dictionary → print the price anyway
#
# Otherwise → print “Unknown item”
#================================Task 5 start========================================
# buy_items = ["milk", "bread", "eggs"]
# prices = {
#     "milk" : 60,
#     "bread" : 35,
#     "eggs" : 80,
#     "sour_cream" : 60,
#     "orange" : 50
#     }
#
# item_search = input("Enter item to search: ")
#
# if item_search in buy_items:
#     print("This item is on your list")
# elif item_search in prices:
#     print(prices[item_search])
# else:
#     print("Unknown item")
#================================Task 5 end==========================================
#
# Challenge 3: User Login System (Simple Version)
#
# Create a list of user dictionaries, where each dictionary has:
# • "username"
# • "password"
# • "active" → True or False
#
# Ask the user to enter a username and password.
# Use if…else to check:
#
# If the username exists
#
# If the password matches
#
# If the user is marked as "active"
#
# Print one clear result:
# • “Login successful” OR
# • “Wrong password” OR
# • “User not active” OR
# • “User not found”
#================================Task 6 start========================================
userlist = [ {
    "username" : "bandera",
    "password" : "slavaukraini",
    "active" : True
},
 {
    "username" : "brancusi",
    "password" : "romanesti",
    "active" : False
}]

username = input("username: ")
password = input("password: ")

the_user = None
for user in userlist:
    if username == user["username"]:  # if user in list
        the_user = user
        if the_user["password"] == password:  # if password matches
            if the_user["active"]:  # if user active
                print("Login successful")
            else:  # if user not active
                print("User not active")
        else:  # if password doesnt match
            print("Wrong password")
        break
if not the_user:# if user not in list
    print("User not found")
#================================Task 6 end==========================================