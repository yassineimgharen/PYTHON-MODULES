try:
    # number = int(input("enter a number: "))
    # print(number)
    open("non_existent_file.txt", "r")
    # raise Exception("an error occurred")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except FileNotFoundError:
    print("File not found")
else:
    print("No errors occurred")
finally:
    print("Execution completed")
