# Define a class named 'Dog'
class Dog:
    # Class attribute (shared by all instances of the class)
    species = "Canis familiaris"

    # Constructor method (__init__) to initialize object attributes
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed # Instance attribute

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Instance method
    def describe(self):
        print(f"{self.name} is a {self.breed} of the species {self.species}.")

# Create objects (instances) of the 'Dog' class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

# Access attributes and call methods on the objects
print(f"Dog 1's name: {dog1.name}")
print(f"Dog 2's breed: {dog2.breed}")
print(f"Dog 1's species: {dog1.species}") # Accessing a class attribute

dog1.bark()
dog2.describe()