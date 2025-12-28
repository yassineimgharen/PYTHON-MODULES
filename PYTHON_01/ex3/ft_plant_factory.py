class Plant:
    """
    Docstring for Plant
    Plant Class that store and display a Plant info
    """
    def __init__(self, name, height, age):
        """
        Initialize a Plant instance
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Return the plant's information as a formatted string
        """
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


print("=== Plant Factory Output ===")

p1 = Plant("Rose", 25, 30)
p2 = Plant("Oak", 200, 365)
p3 = Plant("Cactus", 5, 90)
p4 = Plant("Sunflower", 80, 45)
p5 = Plant("Fern", 15, 120)

print(p1.get_info())
print(p2.get_info())
print(p3.get_info())
print(p4.get_info())
print(p5.get_info())

print("\nTotal plants created: 5")
