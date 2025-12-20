# Exercise 16: Check Palindrome Number
#
# A palindrome number is a number that remains the same when its digits are reversed.
# In simpler terms, it reads the same forwards and backward. For example 121, 5005.

# Write a code to check if given number is palindrome.

# Reverse a number and check it with original number.
#
#     Initialize a variable to store the reversed number (set it to 0 initially).
#     Use a while loop that continues as long as the original number is greater than 0.
#     Inside the loop:
#         Extract the last digit of the original number using the modulo operator (% 10).
#         Update the reversed number: multiply it by 10 and then add the extracted last digit.
#         Update the original number by integer division (// 10) to remove the last digit.
#     After the loop finishes, the reversed number variable will hold the reversed integer.
#     Now, check if it is same as original number

# =====================================ex_16_start=====================================
# # def palindrome_check(num):
# #
# #     original = num
# #
# #     reverse = 0
# #
# #     while num > 0:
# #         last_num = num % 10
# #         reverse = reverse * 10 + last_num
# #         num = num // 10
# #
# #     if reverse == original:
# #         print("Number is palindrome")
# #
# #     else:
# #         print("Number is NOT palindrome")
# #
# # palindrome_check(121)
#
# def palindrome_check2(num):
#
#     reverse = str(num)[::-1]
#
#     if num == int(reverse):
#         print("Number is palindrome")
#
#     else:
#         print("Number is NOT palindrome")
#
# palindrome_check2(1212)
# =====================================ex_16_end=======================================
# Exercise 17: Generate Fibonacci series up to 15 terms
#
# Have you ever wondered about the Fibonacci Sequence?
# It’s a series of numbers in which the next number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1.
#
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
#
# Expected output:
#
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
#

#     Set num1 = 0 and num2 = 1 (first two numbers of the sequence)
#     Run the loop 15 times
#     In each iteration
#         print num1 as the current number of the sequence
#         Add the last two numbers to get the following number result = num1 + num2
#         update values of num1 and num2. Set num1 = num2 and num2 = result

# =====================================ex_17_start=====================================
# num1 = 0
#
# num2 = 1
#
# for times in range(15):
#
#     print(num1, end="  ")
#
#     next_n = num1 + num2
#
#     num1 = num2
#
#     num2 = next_n

# =====================================ex_17_end=======================================
# Exercise 18: Check if a given year is a leap year
#
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365.
# This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
#
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
#
# Write a code find if a given year is a leap year.
#
# Given:
#
# year1 = 2020
# # Output True
#
# year2 = 2025
# # Output False
# =====================================ex_18_start=====================================
# def leap_year_check(year):
#     if year % 4 == 0:
#
#         if year % 100 == 0 and year % 400 != 0:
#             return False
#
#         else:
#             return True
#     else:
#         return False
#
# print(leap_year_check(2025))
#
# # def is_leap_year(year):
# #     if year % 4 != 0:
# #         return False
# #
# #     if year % 100 == 0 and year % 400 != 0:
# #         return False
# #
# #     return True
# =====================================ex_18_end=======================================
# Exercise: 19: Print Alternate Prime Numbers till 20
#
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
#
# For example:
#
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
#
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

# Show Hint
#
#     First, identify all the prime numbers within the given range (1 to 20).

#     Use this hint to identify prime number: Check divisibility from 2 up to the square root of the number.
#     If divisible by any number in this range, it’s not prime.

#     Handle cases for numbers less than or equal to 1 and the number 2 separately.

#     Now, once you have the list of prime numbers, you need to pick every other prime number from that list, starting with the first one using with a specific step.
#

# =====================================ex_19_start=====================================
# from math import sqrt
#
# prime_list = []
#
# for number in range(2, 20):
#         for check in range(2, int(sqrt(number)) + 1):
#             if number % check == 0:
#                 break
#
#         else:
#             prime_list.append(number)
#
# print(prime_list)
#
# alt_prime = prime_list[:: 2]
#
# print(alt_prime)
# =====================================ex_19_end=======================================
# Exercise 20: Print Reverse Number Pattern
#
# Expected Output:
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# =====================================ex_20_start=====================================
# rows = 5
# for num in range(1, 6):
#     for row in range(rows):
#         print(num, end=" ")
#
#     print()
#     rows -= 1
# =====================================ex_20_end=======================================