# Exercise 11: Get each digit from a number in the reverse order.
#
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
#
# Given:
#
# number = 7536
# # Output 6 3 5 7
# =====================================ex_11_start=====================================
# number = 7536
#
# reverse = str(number)[::-1]
#
# for num in reverse:
#     print(num, end=" ")
#
# # while number > 0:
# #     num = number % 10
# #
# #     number = number // 10
# #
# #     print(num, end=" ")
# =====================================ex_11_end=======================================
# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	        0
# Next $10,000	        10
# The remaining	        20
#
# Expected Output:
# For example, suppose the income is 45000

# and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000
# =====================================ex_12_start=====================================
# def get_tax(the_income):
#     twenty = the_income - 20000
#     if twenty < 0:
#         twenty = 0
#
#     ten = the_income - twenty - 10000
#     if ten < 0:
#         ten = 0
#
#     zero = the_income - ten - twenty
#
#     tax = int(ten * 0.1 + twenty * 0.2)
#
#     print(f"{zero}*0% + {ten}*10% + {twenty}*20% = ${tax}")
#
# get_tax(45000)
# =====================================ex_12_end=======================================
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
#
# Write a code to generates a complete multiplication table for numbers 1 through 10.
#
# Expected Output:
#
# 1  2 3 4 5 6 7 8 9 10
# 2  4 6 8 10 12 14 16 18 20
# 3  6 9 12 15 18 21 24 27 30
# 4  8 12 16 20 24 28 32 36 40
# 5  10 15 20 25 30 35 40 45 50
# 6  12 18 24 30 36 42 48 54 60
# 7  14 21 28 35 42 49 56 63 70
# 8  16 24 32 40 48 56 64 72 80
# 9  18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100
# =====================================ex_13_start=====================================
# for number in range(1, 11):
#
#     for num in range(1, 11):
#         print(f"{number * num:<3}", end="")
#
#     print("")
# =====================================ex_13_end=======================================
# Print a downward half-pyramid pattern of stars
#
# * * * * *
# * * * *
# * * *
# * *
# *
# =====================================ex_14_start=====================================
# # number = 5
# #
# # for star in range(number):
# #
# #     for another in range(number):
# #         print("*", end=" ")
# #
# #     print(" ")
# #     number -= 1
#
#
# for star in range(6, 0, -1):
#
#     for another in range(0, star - 1):
#         print("*", end=" ")
#
#     print(" ")


# =====================================ex_14_end=======================================
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
#
# Note here exp is a non-negative integer, and the base is an integer.
#
# Expected output
#
# Case 1:
#
# base = 2
# exponent = 5
#
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
#
# Case 2:
#
# base = 5
# exponent = 4
#
# 5 raises to the power of 4 is: 625
# i.e. (5 *5 * 5 *5 = 625)


# =====================================ex_15_start=====================================
# def exponent(base, exp):
#     print(int(base) ** abs(int(exp)))
#
# exponent(5,4)
# =====================================ex_15_end=======================================