import sys
import math


def parse_coordinates(coord_str):
    parts = coord_str.split(',')
    if len(parts) != 3:
        raise ValueError("Expected exactly three comma-separated values")
    try:
        x_str, y_str, z_str = parts
        return (int(x_str), int(y_str), int(z_str))
    except ValueError as err:
        raise ValueError(err)


point1 = (0, 0, 0)
point2 = (0, 0, 0)

args = sys.argv

if len(args) != 7:
    print(f"Error: Invalid number of arguments. Usage: python3 {args[0]} "
          f"<x1> <y1> <z1> <x2> <y2> <z2>")
    sys.exit(1)
try:
    point1 = (int(args[1]), int(args[2]), int(args[3]))
    point2 = (int(args[4]), int(args[5]), int(args[6]))
except ValueError:
    print("Error: All coordinates must be numericls values.")
    sys.exit(1)

(x, y, z) = point1
(x2, y2, z2) = point2

distance = math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2)

print("=== Game Coordinate System ===")
print(f"Position created: {point1}")
print(f"Position created: {point2}")
print(f"Distance between {point1} and {point2}: {float(distance):.2f}")
print('\nParsing coordinates: "3,4,0"')

parsed_point = parse_coordinates("3,4,0")
print(f"Parsed position: {parsed_point}")
(a, b, c) = parsed_point
parse_coordinates_distance = math.sqrt((0 - a)**2 + (0 - b)**2 + (0 - c)**2)
print(f"Distance between {0, 0, 0} and {parsed_point}: "
      f"{float(parse_coordinates_distance):.2f}")

print('\nParsing invalid coordinates: "abc,def,ghi"')
try:
    parse_coordinates("abc,def,ghi")
except ValueError as err:
    print(f"Error parsing coordinates: {err}")
    print(f"Error details - Type: {type(err).__name__}, Args: (\"{err}\")")

print("\nUnpacking demonstration:")
print(f"Player at position: x={a}, y={b}, z={c}")
print(f"Coordinates: X={a}, Y={b}, Z={c}")
