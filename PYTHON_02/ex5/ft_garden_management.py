class GardenError(Exception):
    """
    Docstring for GardenError
    Custom exception for garden errors.
    """
    pass


class PlantError(GardenError):
    """
    Custom exception for plant related errors.
    """
    pass


class WaterError(GardenError):
    """
    Custom exception for water related errors.
    """
    pass


class Plant:
    """
    Represents a plant with a name, water level, and sunlight hours.
    """
    def __init__(self, name, water, sunlight):
        self.name = name
        self.water = water
        self.sunlight = sunlight


class GardenManager:
    """
    Docstring for GardenManager
    Manages plants and watering in a garden.
    """
    def __init__(self, tank_level):
        """
        Initializes the garden manager with a water tank level.
        """
        self.plants = []
        self.tank_level = tank_level

    def add_plant(self, plant):
        """
        Adds a plant to the garden, raising PlantError for invalid plants.
        """
        try:
            if plant.name is None or plant.name == "":
                raise PlantError("Error adding plant: Plant name cannot"
                                 " be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(e)

    def water_plant(self):
        """
        Waters all plants in the garden, raising WaterError for issues.
        """
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        """
        Checks the health of all plants in the garden.
        Raises ValueError for invalid plant parameters.
        """
        for plant in self.plants:
            try:
                if plant.name is None:
                    raise ValueError("Error: Plant name cannot be empty!\n")
                if plant.water > 10:
                    raise ValueError(f"Error: Water level {plant.water} is "
                                     f"too high (max 10)\n")
                if plant.water <= 0:
                    raise ValueError(f"Error: Water level {plant.water} is "
                                     f"too low (min 2)\n")
                if plant.sunlight < 2:
                    raise ValueError(f"Error: Sunlight hours {plant.sunlight} "
                                     f"is too low (min 2)\n")
                if plant.sunlight > 12:
                    raise ValueError(f"Error: Sunlight hours "
                                     f"{plant.sunlight} is"
                                     f" too high (max 12)\n")
                print(f"{plant.name}: healthy (water: {plant.water}, "
                      f"sun: {plant.sunlight})")
            except ValueError as e:
                print(e)

    def check_tank_level(self):
        """
        Checks the water tank level, raising GardenError if too low (<=0).
        """
        try:
            if (self.tank_level <= 0):
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")


print("=== Garden Management System ===\n")
my_garden = GardenManager(10)
print("Adding plants to garden...")
tomato = Plant("Tomato", 5, 8)
lettuce = Plant("Lettuce", 14, 5)
my_garden.add_plant(tomato)
my_garden.add_plant(lettuce)
my_garden.add_plant(Plant("", 10, 6))
print("")
print("Watering plants...")
my_garden.water_plant()
print("\nChecking plant health...")
my_garden.check_health()
my_garden.tank_level = 0
print("Testing error recovery...")
my_garden.check_tank_level()
print("\nGarden management system test complete!")
