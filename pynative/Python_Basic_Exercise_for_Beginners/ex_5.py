# Write a code to return True if the list’s first and last numbers are the same.
# If the numbers are different, return False.
# Use list indexing.
#
#     Get the first element of the list.
#     Get the last element of the list.
#     Compare these two elements using the equality operator (==).
#
# Given:
def first_last_equal(list):
    return print(list[0] == list[-1])

numbers_x = [10, 20, 30, 40, 10]
first_last_equal(numbers_x)
# # output True

numbers_y = [75, 65, 35, 75, 30]
first_last_equal(numbers_y)
# # Output False



