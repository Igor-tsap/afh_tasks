# OOP Exercise 9: Check object is a subclass of a particular class
#
# Given:
#
# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Puppy(Dog):
#     pass
#
# class Cat:
#     pass
#
# Write a code to check the following
#
#     Dog is a subclass of Animal? –> True
#     Animal is a subclass of Dog? –> False
#     Cat is a subclass of Animal? –> False
#     Puppy is a subclass of Animal –> True

# =====================================ex_9_start=====================================
# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Puppy(Dog):
#     pass
#
# class Cat:
#     pass
#
# print(f"Dog is a subclass of Animal? –> {issubclass(Dog, Animal)}")
# print(f"Animal is a subclass of Dog? –> {issubclass(Animal, Dog)}")
# print(f"Cat is a subclass of Animal? –> {issubclass(Cat, Animal)}")
# print(f"Puppy is a subclass of Animal –> {issubclass(Puppy, Animal)}")
# =====================================ex_9_end=======================================
# OOP Exercise 10: Calculate the area of different shapes using OOP
#
# Given:
#
# You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.
#
# Now, Write a OOP code to calculate the area of each shapes (each subclass must write its own implementation of area() method to calculates its area).
#
# Use the following code
#
# class Shape:
#     def area(self):
#         raise NotImplementedError("Area method must be implemented by subclasses")
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
# # Example of polymorphism
# shapes = [Circle(5), Square(7), Circle(3)]
#
# for shape in shapes:
#     print(shape.area())  # Output: 78.53975, 49, 28.27431
# =====================================ex_10_start=====================================
# class Shape:
#     def area(self):
#         raise NotImplementedError("Area method must be implemented by subclasses")
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
# # Example of polymorphism
# shapes = [Circle(5), Square(7), Circle(3)]
#
# for shape in shapes:
#     print(shape.area())  # Output: 78.53975, 49, 28.27431
# =====================================ex_10_end=======================================