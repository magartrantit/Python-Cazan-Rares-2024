class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def mileage(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car subclass
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency 

    def mileage(self, km_driven):
        fuel_used = km_driven / self.fuel_efficiency
        print(f"Car mileage: Driven {km_driven} km, used {fuel_used:.2f} liters of fuel.")
        return fuel_used

# Motorcycle subclass
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency 

    def mileage(self, km_driven):
        fuel_used = km_driven / self.fuel_efficiency
        print(f"Motorcycle mileage: Driven {km_driven} km, used {fuel_used:.2f} liters of fuel.")
        return fuel_used

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def mileage(self, km_driven, load_weight):
        base_fuel_efficiency = 10 
        adjusted_efficiency = base_fuel_efficiency - (load_weight / 1000) * 0.5
        fuel_used = km_driven / max(adjusted_efficiency, 1) 
        print(f"Truck mileage: Driven {km_driven} km with {load_weight} kg load, used {fuel_used:.2f} liters.")
        return fuel_used

    def towing_capacity_info(self):
        print(f"Truck towing capacity: {self.towing_capacity} kg.")
        return self.towing_capacity

car = Car("Toyota", "Corolla", 2020, fuel_efficiency=30)
print(car.display_info())
car.mileage(150)

motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2018, fuel_efficiency=55)
print(motorcycle.display_info())
motorcycle.mileage(150)

truck = Truck("Ford", "F-150", 2021, towing_capacity=13000)
print(truck.display_info())
truck.mileage(150, 2000)
truck.towing_capacity_info()
