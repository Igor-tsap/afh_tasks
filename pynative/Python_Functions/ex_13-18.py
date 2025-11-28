# =====================================ex_13_start=====================================
# def factorial_func(number):
#     if number <= 0:
#         return 1
#     else:
#         return number * factorial_func(number - 1)
#
# print(factorial_func(5))
# =====================================ex_13_end=======================================
# =====================================ex_14_start=====================================
# square = lambda number: number * number
#
# print(square(5))
# =====================================ex_14_end=======================================
# =====================================ex_15_start=====================================
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_list = list(filter(lambda number: number % 2 == 0, numbers))
#
# print(even_list)
# =====================================ex_15_end=======================================
# =====================================ex_16_start=====================================
# numbers = [1, 2, 3, 4, 5]
#
# doubled_numbers = list(map(lambda number: number * 2, numbers))
#
# print(doubled_numbers)
# =====================================ex_16_end=======================================
# =====================================ex_17_start=====================================
# data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
#
# sorted_list = list(sorted(data, key = lambda number: number[1]))
#
# print(f"The sorted list of tuples based on the second element is: {sorted_list}")
# =====================================ex_17_end=======================================
# =====================================ex_18_start=====================================
# my_addition = lambda x, y: x + y
# my_subtraction = lambda x, y: x - y
#
# def apply_operation(func, x, y):
#     return func(x, y)
#
# print(apply_operation(my_addition,3, 4))
# print(apply_operation(my_subtraction,3, 4))
# =====================================ex_18_end=======================================