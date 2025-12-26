# Task 1: Finding patterns in text
# Create a text string that contains a short paragraph with several email addresses mixed with normal words.
# Use a regular expression to find all email addresses in the text.
# Store the results in a list and print them.
# Briefly explain what part of your regular expression matches the username, the “@” symbol, and the domain.


# =====================================Task 1 start=====================================
# from re import findall
#
# my_string = "some regular and jonson@gmail.com amd also some more tobias@protonmail.com regular words and something@yahoo.com"
#
# print(findall(r"\w+@\w+.\w+", my_string))
# #first \w+ is username
# # @
# # the second part \w+.\w+ is domain

# =====================================Task 1 end=======================================

# Task 2: Validating user input with RegEx
# Ask the user to enter a phone number.
# Use a regular expression to check whether the input matches a specific format (for example: +380-XX-XXX-XX-XX or XXX-XXX-XXXX).
# If the format is correct, print a confirmation message.
# If the format is incorrect, print an error message and explain which part of the input is invalid.

# =====================================Task 2 start=====================================
# from re import findall, search
# phone = input("phone number: ")
#
# # if findall(r"\+380\d{9}", phone): # \ - escape special character (+), "+380", \d{7} - seven digits
# #     print("phone set successfully")
# # else:
# #     print("input is invalid")
#
# if search(r"^\+380(-?\d){9}$", phone): #"^" - beginning, "&" - end of str "-?" - maybe dashes before digits
#     print("phone set successfully")
# else:
#     print("input is invalid")
# =====================================Task 2 end=======================================

# Task 3: Extracting and replacing data
# Create a string that contains dates written in the format DD/MM/YYYY.
# Use a regular expression to extract all dates from the text.
# Convert each extracted date into the format YYYY-MM-DD.
# Replace the original dates in the text with the new format and print the final result.

# =====================================Task 3 start=====================================
# from re import findall, sub
#
# text = "The project started on 12/03/2023, had a review on 25/07/2024, and will end by 01/01/2026."
#
# # my_list = findall(r"\d\d/\d\d/\d{4}", text)
# #
# # new_list = [f"{date_str[6:10]}-{date_str[3:5]}-{date_str[0:2]}" for date_str in my_list]
# #
# # # new_list1 = list(map(lambda date_str: f"{date_str[6:10]}-{date_str[3:5]}-{date_str[0:2]}", my_list ))
# #
# # new_text = f"The project started on {new_list[0]}, had a review on {new_list[1]}, and will end by {new_list[2]}."
# #
# # print(new_text)
#
# new_text = sub(r"(\d\d)/(\d\d)/(\d{4})", r"\3-\2-\1", text)
#
# print(new_text)



# =====================================Task 3 end=======================================