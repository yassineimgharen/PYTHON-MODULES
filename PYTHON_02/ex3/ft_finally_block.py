def water_plants(plant_list):
    """
    Waters the plants in the given list.
    Raises a ValueError if any plant is None.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Plant is None!")
            print(f"Watering {plant}")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


print("=== Garden Watering System ===\n")


def test_watering_system():
    """
    Tests the watering system with normal and error scenarios.
    """
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully\n")

        print("Testing with error...")
        water_plants(["tomato", None, "carrots"])
    finally:
        print("\nCleanup always happens, even with errors!")


test_watering_system()
