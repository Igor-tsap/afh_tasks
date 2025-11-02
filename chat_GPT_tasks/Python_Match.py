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
