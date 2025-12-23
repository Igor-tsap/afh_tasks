# Task 1: Converting between Python dictionaries and JSON
# Create a Python dictionary that represents a person (name, age, city, skills list).
# Convert this dictionary into a JSON string.
# Print the JSON string and verify that the data structure is preserved.
# Then convert the JSON string back into a Python dictionary and print the result.
# Explain in one or two sentences when this conversion is useful in real applications.

# =====================================Task 1 start=====================================
# import json
#
# person1 = {
#     "name": "Petro",
#     "age": 36,
#     "city": "New York",
#     "skills": ["acting", "cooking", "entrenchment"]
#
# }
#
# j_person1 = json.dumps(person1)
#
# print(j_person1)
# print(type(j_person1)) #becomes a JSON string (plain text) , readable by a lot of languages, converted for an exchange.
#
# person1_back = json.loads(j_person1)
#
# print(person1_back)
# print(type(person1_back)) #becomes python dict, readable only by python, but easy to access and manipulate separate items

# =====================================Task 1 end=======================================

# Task 2: Reading and writing JSON files
# Create a Python dictionary with data about several products (id, name, price, in_stock).
# Save this data into a JSON file.
# Read the JSON file back into your program.
# Use a loop to print only the products that are in stock.
# Add basic error handling in case the file does not exist or contains invalid JSON.

# =====================================Task 2 start=====================================
# import json
# from json import JSONDecodeError
#
# products = {
#     "apple": {
#         "id": 1,
#         "price": 20,
#         "in_stock": True
#     },
#     "banana": {
#         "id": 2,
#         "price": 40,
#         "in_stock": False
#     },
#     "tomato": {
#         "id": 3,
#         "price": 50,
#         "in_stock": True
#     }
# }
#
# with open("json_file.json", "w") as file:
#     json.dump(products, file)
#
# try:
#     with open("json_file.json", "r") as file:
#         json.load(file)
#         for product in products:
#             if products[product]["in_stock"]:
#                 print(product)
#
# except FileNotFoundError:
#     print("file does not exist")
#
# except JSONDecodeError:
#     print("invalid JSON")

# =====================================Task 2 end=======================================

# Task 3: Working with nested JSON data
# Create a JSON structure that represents an online order with nested data (customer info, list of items, total price).
# Load this JSON data into Python.
# Access and print specific values from different nesting levels (for example: customer name, each item name, total price).
# Write a short explanation of how nested JSON maps to Python data types (dicts and lists).

# =====================================Task 3 start=====================================
# import json
#
# nested = json.dumps({"name": "Petro", "age": 40, "list_of_items": {"table": 1000, "chair": 500, "vase": 300}})
#
# n_dict = json.loads(nested)
#
# print(n_dict["name"])
#
# for key in n_dict["list_of_items"].keys():
#     print(key, end=" ")
#
# print(f"\nthe sum is: {sum(n_dict["list_of_items"].values())}")
#

# =====================================Task 3 end=======================================
