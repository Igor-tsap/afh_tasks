# =====================================ex_1-5_start=====================================
# class Vehicle:
#
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity = 50):
#         return f"The seating capacity {self.name} is {capacity} passengers."
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# b1 = Bus("Laz", 100, 1500000)
#
# c1 = Car("Lanos", 150, 300000)
#
# print(f"Color: {b1.color}, Vehicle name: {b1.name}, Speed: {b1.max_speed}, Mileage: {b1.mileage}")
# print(f"Color: {c1.color}, Vehicle name: {c1.name}, Speed: {c1.max_speed}, Mileage: {c1.mileage}")
#
# print(b1.seating_capacity())
# =====================================ex_1-5_end=======================================
# =====================================ex_6-8_start=====================================
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         return super().fare() + self.capacity * 10
#
# School_bus = Bus("School Volvo", 12, 50)
#
# print("Total Bus fare is:", School_bus.fare())
#
# print(type(School_bus))
# print(isinstance(School_bus, Vehicle))
# =====================================ex_6-8_end=======================================


