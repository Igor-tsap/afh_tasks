# Here are **3 practical tasks** on **Python Modules**, based on everything you’ve learned so far.
# (Plain text, easy to copy, no code boxes.)
#
# ---
#
# **Task 1: Create Your Own Module**
# Create a separate Python file named `mymath.py` that contains at least two functions:
# • one function that adds two numbers
# • one function that returns the larger of two numbers
# In your main file, import your module and use both functions with user-entered values.
#
# =====================================Task 1 start=====================================
# import chat_GPT_tasks.module
#
# print(chat_GPT_tasks.module.sum_func(int(input("enter number1: ")), int(input("enter number2: "))))
# print(chat_GPT_tasks.module.larger_func(int(input("enter number1: ")), int(input("enter number2: "))))
# =====================================Task 1 end=======================================
#
# **Task 2: Using the `random` Module**
# Use the `random` module to simulate a simple dice roll game.
# Ask the user to choose a number from 1 to 6.
# Use `random.randint` to generate a dice result.
# Use if…else to print:
# • “You win!” if the numbers match
# • “Try again” if they don’t match
#
# =====================================Task 2 start=====================================
# import random
#
# user_number = int(input("enter a number from 1 to 6: "))
#
# dice_number = random.randint(1, 6)
#
# if user_number == dice_number:
#     print("You win!")
# else:
#     print("Try again")
# =====================================Task 2 end=======================================
#
# **Task 3: Working With the `datetime` Module**
# Ask the user to enter their birth year.
# Use the `datetime` module to get the current year.
# Calculate and print the user’s age.
# If the age is under 18, print “You are a minor”;
# otherwise print “You are an adult.”
#
# =====================================Task 3 start=====================================
# import datetime
#
# user_year = int(input("enter your birth year: "))
# age = datetime.date.today().year - user_year
#
# print(f"your age is: {age}")
# =====================================Task 3 end=======================================
#
# If you want, I can also give you a **challenge version** that mixes modules with lists, dictionaries, or functions.
