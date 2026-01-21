# Exercise
# 8: Print
# the
# value
# of
# key ‘history’ from nested dict
#
# =====================================ex_8_start=====================================
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])
# =====================================ex_8_end=======================================
# In the below dictionary, change name to ‘Jessa’.
# =====================================ex_9_start=====================================
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# sampleDict["class"]["student"]["name"] = "Jessa"

# =====================================ex_9_end=======================================
# In Python, we can initialize the keys with the same values.
# =====================================ex_10_start=====================================
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
#
# my_dict = dict.fromkeys(employees, defaults)
# =====================================ex_10_end=======================================
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# =====================================ex_11_start=====================================
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]
#
# new_dict = {}
#
# for key in keys:
#     for item in sample_dict:
#         if key == item:
#             new_dict.update({item: sample_dict[item]})
#
# print(new_dict)
# =====================================ex_11_end=======================================
# Delete
# a
# list
# of
# keys
# from a dictionary
# =====================================ex_12_start=====================================
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
#
# for key in keys:
#     if key in sample_dict:
#         sample_dict.pop(key)
#
# print(sample_dict)
# =====================================ex_12_end=======================================
# While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.
# Write a Python program to check if the value 200 is present in the provided dictionary.
# =====================================ex_13_start=====================================
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
#
# value = 200
# if value in sample_dict.values():
#     print(f"{value} is present")
# =====================================ex_13_end=======================================
# Write a program to rename a key city to a location in the following dictionary.
# =====================================ex_14_start=====================================
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sample_dict.update({"location": sample_dict["city"]})
# sample_dict.pop("city")

# =====================================ex_14_end=======================================
# Write a code to print the key of a minimum value from the following dictionary.
# =====================================ex_15_start=====================================
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# print(min(sample_dict.keys()))
# =====================================ex_15_end=======================================