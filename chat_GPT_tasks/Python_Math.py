# Task 1: Calculate distance between two points
# Ask the user for x1, y1, x2, y2.
# Use the math.sqrt() function to calculate the distance between the points.
# Formula: distance = sqrt((x2 - x1)**2 + (y2 - y1)**2).
# Print the result.
# =====================================Task 1 start=====================================
# import math
#
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))
#
# distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
# print(distance)
# =====================================Task 1 end=======================================
# Task 2: Random number guessing
# Use the random module to generate a number between 1 and 20.
# Ask the user to guess the number.
# If the guess is correct, print “Correct!”.
# If not, print “Wrong, try again”.
# Use a while loop until the user guesses the correct number.
# =====================================Task 2 start=====================================
# import random
#
# while True:
#     random_number = random.randint(1, 20)
#     user_number = int(input("enter a number 1-20: "))
#     if random_number == user_number:
#         print("Correct!")
#         break
#     else:
#         print(f"Wrong, try again, the number is {random_number}")
# =====================================Task 2 end=======================================
# Task 3: Round and power calculation
# Ask the user for a number.
# Print:
# • the number rounded up (using math.ceil)
# • the number rounded down (using math.floor)
# • the number squared (using math.pow)
# All results should be printed on separate lines.
# =====================================Task 3 start=====================================
# import math
#
# user_number = float(input("enter a number: "))
#
# print(f"rounded up: {math.ceil(user_number)}")
# print(f"rounded down: {math.floor(user_number)}")
# print(f"the number squared: {math.pow(user_number, 2)}")
# =====================================Task 3 end=======================================