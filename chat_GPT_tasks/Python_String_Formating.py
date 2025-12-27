
# Task 1: Formatting user information
# Ask the user to enter their name, age, and city.
# Create a formatted string that outputs a full sentence using this data.
# Use at least two different string formatting methods (for example: f-strings and format()).
# Compare the results and write one sentence explaining which method you find more readable and why.
#
# =====================================Task 1 start=====================================
# name = input("your name: ")
#
# age = input("your age: ")
#
# city = input("your city: ")
#
# print(f"My name is {name}, I'm {age} years old, I live in {city}")
#
# print("My name is {}, I'm {} years old, I live in {}".format(name, age, city))
# =====================================Task 1 end=======================================
#
# Task 2: Formatting numbers and calculations
# Create variables for product price, quantity, and tax percentage.
# Calculate the total cost including tax.
# Output a formatted receipt line that shows each value with clear labels.
# Format the total cost to always display two decimal places.
# Explain why numeric formatting is important in financial data.
#
# =====================================Task 2 start=====================================
#
# price = 35
#
# quantity = 5
#
# tax_percentage = 20
#
# total_cost = price * quantity * tax_percentage
#
# print(f"{'=' * 10}RECEIPT{'=' * 10}\n"
#       f"{'price':<20} {price}\n"
#       f"{'quantity':<20} {quantity}\n"
#       f"{'tax':<20} {tax_percentage}\n"
#       f"{'=' * 27}\n"
#       f"{'total cost':<20} {total_cost:.2f}\n")
# =====================================Task 2 end=======================================
#
# Task 3: Formatting dates and aligned output
# Create a list of events, each containing a name and a date.
# Display the events in a clean, aligned table-like output using string formatting.
# Ensure that all event names are left-aligned and all dates are displayed in the same format.
# Write a short explanation of how alignment improves readability in console output.
#
# =====================================Task 3 start=====================================
# from datetime import datetime
#
# events = [
#     {"name": "Conference", "date": "12/03/2023"},
#     {"name": "Project review", "date": "25/07/2024"},
#     {"name": "Release day", "date": "01/01/2026"}
# ]
#
# date1 = datetime.strptime(events[0]["date"], "%d/%m/%Y")
# date2 = datetime.strptime(events[1]["date"], "%d/%m/%Y")
# date3 = datetime.strptime(events[2]["date"], "%d/%m/%Y")
#
# print(f"\n"
#       f"{events[0]['name']:<20}{date1.strftime("%d/%m/%Y")}\n"
#       f"{events[1]['name']:<20}{date2.strftime("%d/%m/%Y")}\n"
#       f"{events[2]['name']:<20}{date3.strftime("%d/%m/%Y")}\n"
# )


# =====================================Task 3 end=======================================
