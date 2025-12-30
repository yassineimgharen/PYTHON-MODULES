class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_problem():
    raise PlantError("The tomato plant is wilting!")


def water_problem():
    raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Errors Demo ===\n")

print("Testing PlantError...")
try:
    plant_problem()
except PlantError as e:
    print(f"Caught PlantError: {e}\n")
print("Testing WaterError...")
try:
    water_problem()
except WaterError as e:
    print(f"Caught WaterError: {e}\n")

print("Testing catching all garden errors...")
try:
    plant_problem()
except GardenError as e:
    print(f"Caught a garden error: {e}")
try:
    water_problem()
except GardenError as e:
    print(f"Caught a garden error: {e}\n")
finally:
    print("All custom error types work correctly!")
