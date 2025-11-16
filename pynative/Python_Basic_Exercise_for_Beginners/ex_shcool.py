# age = int(input("Enter your age: "))

# if 120 > age >= 18 :
#     print("old enough")
# elif 17 > age > 1:
#     print("not old enough")
# else:
#     print("not appropriate age")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} is even" )
#     else:
#         print(f"{number} is not even")

sum_of_numbers = 1

for number in numbers:
    sum_of_numbers *= number

print(sum_of_numbers)