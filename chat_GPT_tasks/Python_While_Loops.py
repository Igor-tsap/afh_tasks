# Create a while loop that prints numbers from 1 to 20, but only the even ones. Use variables, numbers, and operators you already know.
#================================Task 1 start========================================
# number = 1
# while number <= 20:
#     number += 1
#     if number % 2 == 0:
#         print(number)
#================================Task 1 end==========================================
# Ask the user to type a word. Keep asking again in a while loop until the user types the word "stop". When the loop ends, print "Finished".
#================================Task 2 start========================================
# word = input("Enter a word: ")
# while word != "stop":
#     word = input("Enter a word: ")
# else:
#     print("Finished")
#================================Task 2 end==========================================
# Create a list of several fruits. Use a while loop to print each fruit one by one. Stop the loop early if the fruit is "banana".
# Use lists, conditions, and booleans.
#================================Task 3 start========================================
# fruits = ["apple", "orange", "pear", "mango", "banana", "apricot", "pineapple"]
# number = 0
# while  fruits[number] != "banana":
#     print(fruits[number])
#     number += 1
#================================Task 3 end==========================================
# Bonus Challenge: Number Analyzer with While Loop
#
# Create a program that keeps asking the user to enter positive numbers, one at a time.
#
# Your tasks:
#
# Use a while loop to keep asking for numbers until the user types "stop".
#
# Every time the user enters a number:
# • convert it to an integer
# • add it to a list
# • keep track of:
# – total count of numbers
# – the largest number
# – the smallest number
# – the sum of all numbers
#
# When the user types "stop":
# • If no numbers were entered → print "No numbers entered"
# • Otherwise print:
# – the full list of numbers
# – the total count
# – the average (sum / count)
# – the largest number
# – the smallest number
#
# Extra twist:
# • If the user enters something that is not a number or "stop", print "Invalid input" and continue the loop.
#
# If you want, I can also provide a version of this challenge involving dictionaries, match, or functions.
#================================Task 4 start========================================
my_list = []
the_largest_number = 0
the_sum_of_all_numbers = 0
count_of_numbers = len(my_list)

while True:
    user_number = input("Enter a positive number: ")
    if user_number.isdigit():
        my_list.append(int(user_number))
        the_sum_of_all_numbers += int(user_number)
        the_smallest_number = int(user_number)
        for number in my_list:
            if number > the_largest_number:
                the_largest_number = number
            if number < the_smallest_number:
                the_smallest_number = number
        count_of_numbers = len(my_list)
        print("+")
    elif user_number.lower() == "stop":
        if count_of_numbers == 0:
            print("No numbers entered")
        else:
            the_average = the_sum_of_all_numbers / count_of_numbers
            print(f"the list of numbers: {my_list}")
            print(f"the total count: {count_of_numbers}")
            # print(f"the sum of numbers: {the_sum_of_all_numbers}")
            print(f"the average: {the_average}")
            print(f"the largest number: {the_largest_number}")
            print(f"the smallest number: {the_smallest_number}")
        break
    else:
        print("Invalid input")

#================================Task 4 end==========================================