# Encapsulation: Defining a class with attributes and methods
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# Inheritance: Creating a subclass that inherits from a superclass
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def drive(self):  # Polymorphism: Method overriding
        print(f"Driving the {self.make} {self.model} with electric power")

# Abstraction: Hiding the implementation details from the user
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating objects and demonstrating OOP concepts
car1 = Car("Toyota", "Camry")
car1.drive()

electric_car1 = ElectricCar("Tesla", "Model S", "100 kWh")
electric_car1.drive()

dog = Dog()
print("Dog says:", dog.sound())

cat = Cat()
print("Cat says:", cat.sound())
