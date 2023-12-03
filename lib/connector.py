class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Placeholder for the speak method

# Define a derived class that inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create an instance of the Dog class
dog_instance = Dog("Buddy")

# Call the speak method of the Dog class
print(dog_instance.speak())