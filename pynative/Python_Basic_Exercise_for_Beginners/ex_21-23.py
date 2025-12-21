# Exercise 21: Check if a user-entered string contains any digits using a for loop
#
# Expected Output:
#
# Enter a string: Pynative123Python
# The string contains at least one digit.
#
# Enter a string: PYnative
# The string does not contain any digits.
# =====================================ex_21_start=====================================
# def digit_check(string):
#     for item in string:
#         for number in range(10):
#             if str(number) == item:
#                 return True
#
#     return False
#
# print(digit_check("PYnative"))
# =====================================ex_21_end=======================================
# Exercise 22: Capitalize the first letter of each word in a string
#
# Expected Output:
#
# str1 = "pynative.com is for python lovers"
# # Output Pynative.com Is For Python Lovers
# =====================================ex_22_start=====================================
# def cap_words(string):
#     cap_list = list(map(lambda word: word.capitalize(), string.split()))
#
#     my_str = " ".join(cap_list)
#
#     return my_str
#
#
# print(cap_words("pynative.com is for python lovers"))


# =====================================ex_22_end=======================================
# Exercise 23: Create a simple countdown timer using a while loop.
#
# Write a code to create a simple countdown timer of 5 seconds using a while loop.
#
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
#
# Expected Output:
#
# Time remaining: 5 seconds
# Time remaining: 4 seconds
# Time remaining: 3 seconds
# Time remaining: 2 seconds
# Time remaining: 1 seconds
# Time's up!
# =====================================ex_23_start=====================================
from time import sleep

time = 10

while time > 0:
    print(f"Time remaining: {time} seconds")
    sleep(1)
    time -= 1

print("Time's up!")
# =====================================ex_23_end=======================================