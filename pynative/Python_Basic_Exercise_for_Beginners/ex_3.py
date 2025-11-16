# Exercise 3: Print characters present at an even index number
#
# Write a Python code to accept a string from the user and display characters
# present at an even index number.
#
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
#
my_string = input("Enter text: ")
for letter in range(0, len(my_string), 2):
    print(my_string[letter])