# Great! Since you’ve already covered up to **Python If...Else**, you’re ready to explore **Python Match Statements** (introduced in Python 3.10).
# Here are **3 practical exercises** to help you practice pattern matching with `match` / `case`:
#
# ---
#
# ### 🧮 **Exercise 1: Simple Calculator**
#
# **Task:**
# Write a program that asks the user to input an operator (`+`, `-`, `*`, `/`) and two numbers.
# Use a **`match` statement** to perform the correct operation and print the result.
#
# **Example:**
#
# ```python
# Input:
# Enter operator: *
# Enter first number: 4
# Enter second number: 3
#
# Output:
# Result: 12
# ```
#
# **Hint:**
# Use:
#
# ```python
# match operator:
#     case '+':
#         ...
#     case '-':
#         ...
# ```
#
#================================Task 1 start=======================================
# operator = input("Enter operator(`+`, `-`, `*`, `/`): ")
# first_number = input("Enter first number: ")
# second_number = input("Enter second number: ")
# match operator:
#     case "+":
#         print(int(first_number) + int(second_number))
#     case "-":
#         print(int(first_number) - int(second_number))
#     case "*":
#         print(int(first_number) * int(second_number))
#     case "/":
#         print(int(first_number) / int(second_number))
#     case _:
#         print("invalid operator")
#================================Task 1 end=========================================
#
# ### 📅 **Exercise 2: Day of the Week**
#
# **Task:**
# Ask the user to enter a number (1–7).
# Use a **`match` statement** to print the corresponding day of the week.
# If the number is not between 1 and 7, print `"Invalid day number!"`.
#
# **Example:**
#
# ```python
# Input: 3
# Output: Wednesday
# ```
#
# **Hint:**
# Handle the default case using:
#
# ```python
# case _:
#     print("Invalid day number!")
# ```
#
#================================Task 2 start=======================================
# number = int(input("Enter a number (1-7): "))
# match number:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("invalid day number")
#================================Task 2 end=========================================
#
# ### 🚦 **Exercise 3: Traffic Light Action**
#
# **Task:**
# Create a program that asks the user to enter a traffic light color (`"red"`, `"yellow"`, or `"green"`).
# Use a **`match` statement** to print what the driver should do:
#
# * `"red"` → `"Stop!"`
# * `"yellow"` → `"Get ready!"`
# * `"green"` → `"Go!"`
# * otherwise → `"Invalid color!"`
#
# **Example:**
#
# ```python
# Input: green
# Output: Go!
# ```
#
#================================Task 3 start=======================================
# color = input("Enter a color (green, red or yellow): ")
# match color:
#     case "red":
#         print("STOP!")
#     case "green":
#         print("GO!")
#     case "yellow":
#         print("Get ready!")
#     case _:
#         print("invalid color")
#================================Task 3 end=========================================
#
# Would you like me to add a **“bonus challenge”** that mixes `match`, `if...else`, and `dictionaries` for more advanced logic?
# Bonus Challenge:
# Create a program that works like a small product recommendation system.
#
# Make a dictionary where the keys are product categories (for example: "phone", "laptop", "tablet") and the values are dictionaries that contain:
# • "price"
# • "brand"
# • "stock" (number of items available)
#
# Ask the user to enter a category name.
#
# Use a match statement to check which category was requested:
# • If the category exists, then use if...else logic to:
# – Print the product info from the dictionary
# – Check if stock > 0 → print “Available”
# – Else → print “Out of stock”
# • If the category does not match any option, print “Unknown category”.
#
# As an extra step, allow the user to type “discount” to apply a 10% price reduction to the chosen product (use if...else inside the match case).
#================================Task 4 start=======================================


category = {
    "phone" : {
        "price" : 1000,
        "brand" : "apple",
        "stock" : 11
    },
    "laptop" : {
        "price" : 1200,
        "brand" : "dell",
        "stock" : 0
    },
    "tablet" : {
        "price" : 1100,
        "brand" : "samsung",
        "stock" : 100
    }
}

user_input = input("Enter category name: ")

# match user_input:
#     case "phone":
#         if category["phone"]["stock"] < 1:
#             print("Out of stock")
#         else:
#             if input("Do you want a discount? ") != "no":
#                 category["phone"]["price"] *= 0.9
#                 print(f"{category["phone"]["brand"]} is available, the price is: {category["phone"]["price"]}")
#             else:
#                 print(f"{category["phone"]["brand"]} is available, the price is: {category["phone"]["price"]}")
#     case "laptop":
#         if category["laptop"]["stock"] < 1:
#             print("Out of stock")
#         else:
#             if input("Do you want a discount? ") != "no":
#                 category["laptop"]["price"] *= 0.9
#                 print(f"{category["laptop"]["brand"]} is available, the price is: {category["laptop"]["price"]}")
#             else:
#                 print(f"{category["laptop"]["brand"]} is available, the price is: {category["laptop"]["price"]}")
#     case "tablet":
#         if category["tablet"]["stock"] < 1:
#             print("Out of stock")
#         else:
#             if input("Do you want a discount? ") != "no":
#                 category["tablet"]["price"] *= 0.9
#                 print(f"{category["tablet"]["brand"]} is available, the price is: {category["tablet"]["price"]}")
#             else:
#                 print(f"{category["tablet"]["brand"]} is available, the price is: {category["tablet"]["price"]}")
#     case _:
#         print("Unknown category")

def my_function(item):
    if category[item]["stock"] < 1:
        print("Out of stock")
    else:
        if input("Do you want a discount? ") != "no":
            category[item]["price"] *= 0.9
            print(f"{category[item]["brand"]} is available, the price is: {category[item]["price"]}")
        else:
            print(f"{category[item]["brand"]} is available, the price is: {category[item]["price"]}")


match user_input:
    case "phone":
        my_function("phone")
    case "laptop":
        my_function("laptop")
    case "tablet":
        my_function("tablet")
    case _:
        print("Unknown category")
#================================Task 4 end=========================================