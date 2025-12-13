# =====================================ex_8_start=====================================
# totalMoney = 1000
# quantity = 3
# price = 450
#
# # print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price:.2f} dollars.")
#
# print("I have {} dollars so I can buy {} football for {:.2f} dollars.".format(totalMoney, quantity, price))
# =====================================ex_8_end=======================================
# =====================================ex_9_start=====================================
# from os import stat
#
# if stat("test.txt").st_size:
#     print("file NOT empty")
# else:
#     print("empty file")
# =====================================ex_9_end=======================================
# =====================================ex_10_start=====================================
# # print(open("test.txt").readlines()[3])
#
# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     print(lines[3])
# =====================================ex_10_end=======================================
# Ask the user for a numerator and a denominator.
# Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).
# =====================================ex_11_start=====================================
# numerator = int(input("enter numerator: "))
# denominator = int(input("enter denominator: "))
#
# percentage = (numerator/denominator) * 100
# print(f"The percentage of {numerator}/{denominator} is {percentage:.2f}%")
# =====================================ex_11_end=======================================
# Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”.
# Based on the user’s input, perform the corresponding action
# =====================================ex_12_start=====================================
# user_name = input("enter your name: ")
#
# print(f"Hello, {user_name}!")
#
# while True:
#     number = int(input("Would you like to 1.Calculate Square or 2.Exit (enter number): "))
#
#     if number == 1:
#         num1 = int(input("enter a number: "))
#         print(f"Square of {num1} is {num1 ** 2}")
#
#     elif number == 2:
#         print(f"Buy {user_name}")
#         break
#
#     else:
#         print(f"invalid choice {user_name}")
# =====================================ex_12_end=======================================
# Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.
# =====================================ex_13_start=====================================
# user_word = input("word: ")
# user_num = input("number: ")
#
# print(f"{user_word:>20} {user_num}")
# =====================================ex_13_end=======================================
# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].
# Print these lists as a simple table with columns “Name” and “Score”.
#
# Expected Output:
#
# Name       Score
# ---------------
# Alice      85
# Bob        92
# Charlie    78
# =====================================ex_14_start=====================================
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
#
# # table = zip(names, scores)
# #
# # print(f"Name {"Score":>10}\n"
# #       "---------------"
# # )
# #
# # for item in table:
# #     print(f"{item[0]} {item[1]:>{11 - len(item[0])}}")
#
# print(f"{"Name":<10}{"Score":<10}\n"
#       "---------------"
# )
#
# for name, score in zip(names, scores):
#     print(f"{name:<10}{score:<10}")
# =====================================ex_14_end=======================================
# Ask the user for a number. Print this number padded with leading zeros to a width of 5.
#
# For example, if the input is 12, the output should be “00012“
# + Show Hint
#
#     Get the number as a string using input().
#     Use the zfill() string method to pad it with leading zeros to the desired width.
# =====================================ex_15_start=====================================
# user_num = input("enter num: ")

# print(user_num.zfill(5))
# =====================================ex_15_end=======================================
