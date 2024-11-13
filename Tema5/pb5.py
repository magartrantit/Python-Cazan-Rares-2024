class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Mammal(Animal):
    def __init__(self, name, age, fur_type):
        super().__init__(name, age)
        self.fur_type = fur_type

    def speak(self):
        print(f"{self.name} makes a mammalian sound.")

    def move(self):
        print(f"{self.name} walks or runs.")

    def nurse_young(self):
        print(f"{self.name} is nursing its young.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def speak(self):
        print(f"{self.name} chirps or sings.")

    def move(self):
        print(f"{self.name} flies.")

    def lay_eggs(self):
        print(f"{self.name} lays eggs.")

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def speak(self):
        print(f"{self.name} makes bubbling sounds (if any).")

    def move(self):
        print(f"{self.name} swims.")

    def breathe_underwater(self):
        print(f"{self.name} is breathing underwater.")

mammal = Mammal("Lion", 5, fur_type="short")
print(f"Mammal: {mammal.name}, Age: {mammal.age}, Fur type: {mammal.fur_type}")
mammal.speak()
mammal.move()
mammal.nurse_young()

bird = Bird("Eagle", 3, wing_span=2.5)
print(f"Bird: {bird.name}, Age: {bird.age}, Wing span: {bird.wing_span} meters")
bird.speak()
bird.move()
bird.lay_eggs()

fish = Fish("Salmon", 2, water_type="freshwater")
print(f"Fish: {fish.name}, Age: {fish.age}, Water type: {fish.water_type}")
fish.speak()
fish.move()
fish.breathe_underwater()
