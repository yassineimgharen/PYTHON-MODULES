#!/usr/bin/env python3
def garden_operations(n: int):
    if (n == 0):
        print(int("abd"))
    if (n == 1):
        print(10 / 0)
    if (n == 2):
        open("non_existent_file.txt", "r")
    if (n == 3):
        d = {}
        print(d["missing_key"])


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    for i in range(4):
        try:
            garden_operations(i)
        except ValueError:
            print("Testing ValueError...")
            print("Caught ValueError: invalid literal for int()\n")
        except ZeroDivisionError:
            print("Testing ZeroDivisionError...")
            print("Caught ZeroDivisionError: division by zero\n")
        except FileNotFoundError:
            print("Testing FileNotFoundError...")
            print("Caught FileNotFoundError: No such file ", end="")
            print("non_existent_file.txt\n")
        except KeyError:
            print("Testing KeyError...")
            print("Caught KeyError: 'missing_key'\n")
    try:
        garden_operations(1)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


test_error_types()
