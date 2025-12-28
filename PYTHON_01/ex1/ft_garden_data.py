#!/usr/bin/env python3
class Plant:
    def __init__(self):
        """
        Initialize a Plant instance
        """
        pass


p1 = Plant()
p1.name = "Rose"
p1.height = 25
p1.age = 30

p2 = Plant()
p2.name = "Sunflower"
p2.height = 85
p2.age = 45

p3 = Plant()
p3.name = "Cactus"
p3.height = 15
p3.age = 120

print("=== Garden Plant Registry ===")
print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
print(f"{p3.name}: {p3.height}cm, {p3.age} days old")
