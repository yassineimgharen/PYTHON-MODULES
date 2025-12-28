def check_temperature(temp_str):
    try:
        temp_int = int(temp_str)
        if (temp_int < 0):
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
            return None
        elif (temp_int > 40):
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
            return None
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!\n")
            return temp_int
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input():
    test_inputs = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for temp in test_inputs:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)

    print("All tests completed - program didn't crash!")


test_temperature_input()
