# Here are 3 practical Python Range challenges, using only the topics you listed and nothing extra:
#
# Create a program that prints all even numbers from 2 to 20 using a range.
# After printing, show how many numbers were printed using len() on a list you created.
# =====================================Task 1 start=====================================
# # my_even_list = [x for x in list(range(2, 20)) if x % 2 == 0]
#
# my_even_list = list(range(2, 20, 2))
#
# print(my_even_list)
# print(f"numbers printed: {len(my_even_list)}")
# =====================================Task 1 end=======================================
# Ask the user for a number.
# Use a range to print all numbers from 1 up to that number.
# If the number is less than 1, print a message saying it is invalid.
# =====================================Task 2 start=====================================
# user_number = int(input("enter a number: "))
#
# if user_number < 1:
#     print("invalid number")
# else:
#     print(list(range(1, user_number)))
# =====================================Task 2 end=======================================
# Create a list using range that contains every 3rd number from 0 to 30.
# Then use if...else to check: if the number 15 is in the list, print “Found 15”, otherwise print “15 not in list”.
# =====================================Task 3 start=====================================
# my_list = list(range(0, 30, 3))
#
# # num15 = False
# #
# # for number in my_list:
# #     if number == 15:
# #         num15 = True
# #         break
# #
# # if num15:
# #     print("Found 15")
# # else:
# #     print("15 not in list")
#
# if 15 in my_list:
#     print("found 15")
# else:
#     print("15 not in list")
# =====================================Task 3 end=======================================