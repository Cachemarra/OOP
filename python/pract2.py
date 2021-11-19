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

#%% Practice 2. Creation of two children clases 
# The children classes will inherit from Figure and Colour classes.
# Square children will have an get_area() method and override __str__.
# Rectangle children will have an get_area() method and override __str.
# Father class Figure will have 2 paremeters (widht, height) and 4 methods:
# __str__, get_height(), set_height(height), get_width(), set_width()
# Colour class will have "colour" parameter and 2 methods, get_colour & set_colour(colour)

# Father Classes
class Figure:
    def __init__(self, height: float, width: float) -> None:
        self._height = height
        self._width = width
    # Override
    def __str__(self):
        return f'FigureClass: [height: {self._height}, width: {self._width}]'

    # semi-Encapsulation
    def get_height(self):
        return self._height
    
    def set_height(self, height):
        self._height = height
        
    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width


class Colour:
    def __init__(self, colour: str) -> None:
        self._colour = colour

    # Semi-Encapsulation
    def get_colour(self):
        return self._colour
    
    def set_colour(self, colour: str):
        self._colour = colour

# Children Classes.
class Square(Figure, Colour):
    # Overriding __init__+
    def __init__(self, side: float, colour: str) -> None:
        # Calling the __init__ method from both parents
        Figure.__init__(self, height=side, width=side)
        Colour.__init__(self, colour=colour)

    # Method to calculate square area
    def get_area(self):
        return self._height * self._width
    
    def __str__(self):
        return f'SquareClass [area: {self.get_area()}], {super().__str__()}'


class Rectangle(Figure, Colour):
    # Overriding
    def __init__(self, height: float, width: float, colour: str) -> None:
        Figure.__init__(self, height=height, width=width)
        Colour.__init__(self, colour)

    def get_area(self):
        return self._height * self._width
    
    def __str__(self):
        return f'RectangleClass [area: {self.get_area()}], {super().__str__()}'


# Test
print('SquareClass'.center(40, '-'))
square = Square(side= 6, colour='Green')
print(f'SquareArea: {square.get_area()}')
print(square)

square.set_height(5)
square.set_width(5)
square.set_colour('Gray')
print(f'SquareArea: {square.get_area()}')
print(square)

print('RectangleClass'.center(40, '-'))
rectangle = Rectangle(height=3, width=5, colour='Blue')
print(f'RectangleArea: {rectangle.get_area()}')
print(rectangle)

rectangle.set_width(10); rectangle.set_height(2)
rectangle.set_colour('Emerald')
print(f'RectangleArea: {rectangle.get_area()}')
print(rectangle)


# %%
