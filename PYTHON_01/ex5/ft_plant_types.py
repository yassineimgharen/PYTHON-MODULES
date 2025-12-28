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


class Flower(Plant):
    """
    Docstring for Flower
    Flower Class that store and display a Flower info
    """
    def __init__(self, name, height, age, color):
        """
        Initialize a Flower instance
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Docstring for Tree
    Tree Class that store and display a Tree info
    """
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    """
    Docstring for Vegetable
    Vegetable Class that store and display a Vegetable info
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initialize a Vegetable instance
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


flower1 = Flower("Rose", 25, 30, "red")
flower2 = Flower("Tulip", 40, 1, "yellow")

tree1 = Tree("Oak", 500, 1825, 50)
tree2 = Tree("Pine", 300, 1095, 30)

vagatable1 = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
vegetable2 = Vegetable("Carrot", 60, 120, "fall", "high in beta-carotene")

print("=== Garden Plant Types ===")
print(f"\n{flower1.name} (Flower): {flower1.height}cm, {flower1.age} days"
      f", {flower1.color} color")

flower1.bloom()
print(f"\n{tree1.name} (Tree): {tree1.height}cm, {tree1.age} days"
      f", {tree1.trunk_diameter}cm diameter")

tree1.produce_shade()
print(f"\n{vagatable1.name} (Vegetable): {vagatable1.height}cm"
      f", {vagatable1.age} days, {vagatable1.harvest_season} harvest")

print(f"{vagatable1.name} is {vagatable1.nutritional_value}")
