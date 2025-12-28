class SecurePlant:
    """
    Docstring for SecurePlant
    SecurePlant Class that store and display a Plant info with security checks
    """
    def __init__(self, name, height, age):
        """
        Initialize a Plant instance
        """
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height):
        """
        Set the height of the plant with security checks
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height} cm [REJECTED]"
                  f".\nSecurity: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.get_height()}cm [OK]")

    def get_height(self):
        """
        Get the height of the plant
        """
        return self.__height

    def set_age(self, age):
        """
        Set the age of the plant with security checks
        """
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]"
                  f".\nSecurity: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_age(self):
        """
        Get the age of the plant
        """
        return self.__age


plant1 = SecurePlant("rose", 10, 5)

print("=== Garden Security System ===")
print("Plant created: " + plant1.name)
plant1.set_height(-5)
plant1.set_age(30)
print(f"\nCurrent plant: {plant1.name} ({plant1.get_height()}"
      f"cm, {plant1.get_age()} days)")
