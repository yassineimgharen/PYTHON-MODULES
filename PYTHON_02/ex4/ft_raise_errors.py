def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Checks the health of a plant based on its water and sunlight levels.
    Raises ValueError for invalid parameters.
    """
    try:
        if plant_name is None:
            raise ValueError("Error: Plant name cannot be empty!\n")
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} is "
                             f"too high (max 10)\n")
        if water_level <= 0:
            raise ValueError(f"Error: Water level {water_level} is "
                             f"too low (min 2)\n")
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)\n")
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is"
                             f" too high (max 12)\n")
        print(f"Plant {plant_name} is healthy!\n")
    except ValueError as e:
        print(e)


print("=== Garden Plant Health Checker ===\n")


def test_plant_checks():
    """
    Tests the plant health checking function with deffirent inputs.
    """
    print("Testing good values...")
    check_plant_health("Tomato", 5, 6)

    print("Testing empty plant name...")
    check_plant_health(None, 5, 6)

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 6)

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, -15)

    print("All error raising tests completed!")


test_plant_checks()
