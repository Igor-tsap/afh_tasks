# Below are three practical tasks focused on **Python OOP**.
# They are written in plain English, easy to copy, and explicitly aligned with the OOP topics you have already completed
# (classes, init, self, properties, methods, inheritance, polymorphism, encapsulation, inner classes).
#
# Task 1: Basic class design and encapsulation
# Design a class called Account that represents a bank account.
# The class should store the account owner’s name and a private balance attribute.
# Create methods to deposit money, withdraw money, and display the current balance.
# Ensure that the balance cannot be accessed or modified directly from outside the class.
# Write a short explanation of how encapsulation is applied in this design.
#
# =====================================Task 1 start=====================================

# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         return  f"The balance is: {self.__balance}"
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         self.__balance -= amount
#
# p1 = Account("Mykola", 10000)
#
# print(p1.name)
#
# try:
#     print(p1.balance)
#
# except AttributeError:
#     print(f"\n{'=' * 30}\nbalance is a private attribute\n{'=' * 30}\n")
#
# p1.deposit(300)
#
# print(p1.get_balance())
#
# p1.withdraw(100)
#
# print(p1.get_balance())

# =====================================Task 1 end=======================================
#
# Task 2: Inheritance and polymorphism
# Create a base class called Employee with properties for name and base salary.
# Add a method called calculate_salary that returns the base salary.
# Create two child classes, for example Developer and Manager, that inherit from Employee.
# Override the calculate_salary method in each child class to apply different bonus logic.
# Use a loop to calculate and print salaries for different employee objects and explain how polymorphism works in this example.
#
# =====================================Task 2 start=====================================
# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.salary = base_salary
#
#     def calculate_salary(self):
#         return self.salary
#
# class Developer(Employee):
#
#     def calculate_salary(self):
#         return self.salary * 1.5
#
# class Manager(Employee):
#
#     def calculate_salary(self):
#         return self.salary * 2.0
#
# d1 = Developer("Maksym", 3000)
#
# m1 = Manager("Tolik", 3000)
#
# for employee in [d1, m1]:
#     print(f"{employee.name}'s salary is: {employee.calculate_salary()}")

# =====================================Task 2 end=======================================
#
# Task 3: Inner classes and object relationships
# Create a class called Order that contains an inner class called Item.
# Each Item should have a name, price, and quantity.
# The Order class should store multiple Item objects and calculate the total order cost.
# Demonstrate creating items and adding them to an order.
# Explain when using an inner class makes sense compared to defining the class separately.
#
# =====================================Task 3 start=====================================
# class Order:
#     def __init__(self, number):
#         self.number = number
#         self.items = []
#
#     class Item:
#         def __init__(self, name, price, quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def total_cost(self):
#         cost = 0
#
#         for item in self.items:
#             cost += item.price * item.quantity
#
#         return cost
#
# o1 = Order(1)
#
# i1 = o1.Item("banana", 20, 5)
# i2 = o1.Item("apple", 10, 10)
# i3 = o1.Item("orange", 50, 3)
#
# o1.add_item(i1)
# o1.add_item(i2)
# o1.add_item(i3)
#
# print(o1.total_cost())

# =====================================Task 3 end=======================================