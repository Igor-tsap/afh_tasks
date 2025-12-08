# =====================================ex_1_start=====================================
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
#
# print(f"original dict: {my_dict}")
#
# my_dict.update({'profession': 'Doctor'})
#
# print(f"dict with profession added: {my_dict}")
#
# my_dict["age"] = 40
#
# print(f"dict with age updated: {my_dict}")
#
# print(f"city: {my_dict["city"]}")
# =====================================ex_1_end=======================================
# =====================================ex_2_start=====================================
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#
# print(f"original dict: {my_dict}")
#
# del my_dict["profession"]
#
# print("            ")
# print(f"dict with del profession: {my_dict}")
#
# print("            ")
# print(f"print key-value pairs: ")
#
# for item in my_dict:
#     print(f"{item}: {my_dict[item]}")
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
#
# print("         ")
#
# if "age" in my_dict:
#     print("age exists")
# =====================================ex_2_end=======================================
# =====================================ex_3_start=====================================
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# my_dict = {}
#
# index = 0
# for key in range(len(keys)):
#     my_dict.update({keys[index]: values[index]})
#     index += 1
#
# print(my_dict)
# =====================================ex_3_end=======================================
# =====================================ex_4_start=====================================
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
#
# my_dict.clear()
#
# print(my_dict)
# =====================================ex_4_end=======================================
# =====================================ex_5_start=====================================
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# # dict3 = dict1 | dict2
# # print(dict3)
#
# # for key, value in dict2.items():
# #     dict1.update({key: value})
# for item in dict2:
#     dict1.update({item: dict2[item]})
#
# print(dict1)
# =====================================ex_5_end=======================================
# =====================================ex_6_start=====================================
# string1 = 'Jessa'
#
# freq_dict = {}
#
# for letter in string1:
#     if letter not in freq_dict:
#         freq_dict.update({letter: 1})
#     else:
#         freq_dict[letter] += 1
#
# print(freq_dict)
# =====================================ex_6_end=======================================
# =====================================ex_7_start=====================================
# data = {'person': {'name': 'Alice', 'age': 30}}
#
# print(f"Alice's age is {data["person"]["age"]}")
# =====================================ex_7_end=======================================