#!/usr/bin/env python3
class Plant:
    """
    Docstring for Plant class
    Plant Class that store and display a Plant info
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Docstring for __init__
        Initialize a Plant instance
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """
        Increase the height of the plant
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self) -> None:
        """
        Print the plant's description
        """
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """
    Docstring for FloweringPlant class
    FloweringPlant Class that store and display a FloweringPlant info
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a FloweringPlant instance
        """
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True

    def describe(self):
        """
        Print the plant's description
        """
        state = "blooming" if self.blooming else "not blooming"
        print(f"- {self.name}: {self.height}cm,", end="")
        print(f" {self.color} flowers ({state})")


class PrizeFlower(FloweringPlant):
    """
    Docstring for PrizeFlower class
    PrizeFlower Class that store and display a PrizeFlower info
    """
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int):
        """
        Initialize a PrizeFlower instance
        """
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.blooming = True

    def describe(self):
        """
        Print the plant's description
        """
        state = "blooming" if self.blooming else "not blooming"
        print(f"- {self.name}: {self.height}cm, {self.color}", end="")
        print(f" flowers ({state}), Prize points: {self.prize_points}")


class Garden:
    """
    Docstring for Garden class
    Garden Class that manage a collection of plants
    """

    grow_count = 0

    def __init__(self, name: str):
        """
        Initialize a Garden instance
        """
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        """
        Add a plant to the garden
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow(self):
        """
        Grow all plants in the garden
        """
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            Garden.grow_count += 1


class GardenManager:
    """
    Docstring for GardenManager class
    GardenManager Class that manage a collection of plants
    """
    total_gardens = 0
    gardens = {}

    @classmethod
    def add_garden(cls, garden):
        """
        Add a garden to the manager
        """
        if garden.name in cls.gardens:
            print(f"Garden for {garden.name} already exists.")
        else:
            cls.gardens[garden.name] = garden
        cls.total_gardens += 1

    @classmethod
    def create_garden_network(cls):
        return cls()

    class GardenStats:
        """
        Docstring for GardenStats class
        GardenStats Class that provide statistics about gardens
        """
        @staticmethod
        def height_validation(height):
            """
            Validate if the height positive
            """
            return height >= 0

        @staticmethod
        def report(garden: Garden):
            """
            Docstring for get_plants_info
            Display plants description
            """
            print("=== Alice's Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                plant.describe()
            print("")
            print(f"Plants added: {len(garden.plants)}, Total", end="")
            print(f" growth: {Garden.grow_count} cm")
            regular = flowering = prize_flowers = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize_flowers += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            print(f"Plant types: {regular} regular,", end="")
            print(f" {flowering} flowering, {prize_flowers} prize flowers")

        @staticmethod
        def total_prize_points(garden: Garden) -> int:
            """
            Return the total prize points from PrizeFlowers in the garden
            """
            total_points = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    total_points += plant.prize_points
            return total_points

        @classmethod
        def garden_scores(cls, manager: "GardenManager"):
            """
            Print the garden scores based on prize points
            """
            print("Garden scores - ", end="")
            items = list(manager.gardens.items())
            for i, (owner, garden) in enumerate(items):
                score = cls.total_prize_points(garden)
                end = ", " if i < len(items) - 1 else ""
                print(f"{owner}: {score}", end=end)
            print()


print("=== Garden Management System Demo ===")
print("")
manager = GardenManager.create_garden_network()
alice_garden = Garden("Alice")
bob_garden = Garden("Bob")
manager.add_garden(alice_garden)
manager.add_garden(bob_garden)
plant_1 = Plant("Oak Tree", 100, 1825)
plant_2 = FloweringPlant("Rose", 25, 30, "red")
plant_3 = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
alice_garden.add_plant(plant_1)
alice_garden.add_plant(plant_2)
alice_garden.add_plant(plant_3)
print("")
alice_garden.grow()
print("")
manager.GardenStats.report(alice_garden)
print("")
print(f"Height validation test: {manager.GardenStats.height_validation(25)}")
manager.GardenStats.garden_scores(GardenManager)
print(f"Total gardens managed: {GardenManager.total_gardens}")
