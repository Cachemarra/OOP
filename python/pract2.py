#%% Pract 2
# Creation of a father class called Vehicle and two childrens: Car and Bicycle
# Father class must have 2 attributes, Color and tires and 2 methods: __init__, __str__
# Car class must inherit all from father plus an attribute velocity (km/hr) and override methods __init__, __str__
# Bicycle mus have attribute "type: str" and override __init__, __str__ methods

# Father class. Remember, it inherits from Object class by default!
class Vehicle:
    def __init__(self, color: str, tires: int) -> None:
        self.color = color
        self.tires = tires
    
    def __str__(self):
        return f'VehicleClass: [{self.color}, {self.tires}]'


# First children: Car
class Car(Vehicle):
    def __init__(self, color: str, tires: int, velocity: float) -> None:
        super().__init__(color, tires)
        self.velocity = velocity
    # OVerriding __str__
    def __str__(self):
        return f'CarClass: [km/hr: {self.velocity}], {super().__str__()}'

# Second children: Bicycle
class Bicycle(Vehicle):
    def __init__(self, color: str, tires: int, type: str) -> None:
        super().__init__(color, tires)
        self.type = type

    # Overriding __str__
    def __str__(self):
        return f'BicycleClass: [type: {self.type}], {super().__str__()}'


# Test the classes´
if __name__ == '__main__':
    # Test Vehicle Class
    vehicle = Vehicle('red', 3)
    print(vehicle)

    # Test Car class
    car = Car('blue', 4, 100)
    print(car)

    # Test Bicycle class
    bicycle = Bicycle('Black', 2, 'mountain')
    print(bicycle)


# %%
