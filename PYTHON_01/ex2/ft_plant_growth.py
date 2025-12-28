class Plant:
    """
    Docstring for Plant class
    Plant Class that store and display a Plant info
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm):
        """
        Increase the height of the plant
        """
        self.height += cm

    def increase_age(self, age_days):
        """
        Increase the age of the plant
        """
        self.age += age_days

    def get_info(self):
        """
        Return the plant's information as a formatted string
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


p1 = Plant("Rose", 25, 30)
p2 = Plant("Sunflower", 85, 45)
p3 = Plant("Cactus", 15, 120)

print("=== Day 1 ===")
print(f"{p1.name}: {p1.height}cm, {p1.age} days old")

for i in range(1, 7):
    print(f"=== Day {i + 1} ===")
    p1.grow(1)
    p1.increase_age(1)
    print(p1.get_info())

print(f"Growth this week: +{i}cm")
