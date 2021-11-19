#%% First practice
# Creation of an arithmetic class to add, sub, mult and division

class Arith:
    """
    Arithmetic class that allows multiplication, division, add and substraction
    """

    # Constructor
    def __init__(self, numA, numB):
        self.numA = numA
        self.numB = numB

    # Addition operand function
    def add(self):
        return self.numA + self.numB

    # Substraction function
    def sub(self):
        return self.numA - self.numB

    # Multiplication method
    def mul(self):
        return self.numA * self.numB
    
    # Division method
    def div(self):
        return self.numA / self.numB




#%% Test

if __name__ == '__main__':

    calculator = Arith(5, 3)

    print(f'Addition: {calculator.add()}')
    print(f'Substraction: {calculator.sub()}')
    print(f'Multiplication: {calculator.mul()}')
    print(f'Division: {calculator.div()}')        


# %% Creation of a class rectangle.
# A class with parameters "base", height
# A method that returns the area

class Rectangle:
    """
    A rectangle class whose parameters are base and height and a 
    method called calc_area
    """
    # Constructor
    def __init__(self, base: int or float, height: int or float) -> None:
        self.base = base
        self.height = height
        self.area = 0

    def calc_area(self) -> float:
        self.area = self.base * self.height
        return self.area

# Test
if __name__ == '__main__':

    base = 0; height = 0
    if base == 0 and height == 0:

        print('Give me the base: ')
        base = float(input('base = '))
        print('Give me the height:')
        height = float(input('height = '))

    # Object instance
    rect = Rectangle(base, height)

    print('The rectangle area is: ')
    print(rect.calc_area())


# %% Creation of a cube class
# Will have an calc volume method

class Cube:
    """
    A class to calculate cube volume
    """

    # Constructor
    def __init__(self, height:float, width:float, deep:float) -> None:
        self.height = height
        self.width = width
        self.deep = deep
        self.volume = 0

    # Method volume calculation
    def calc_vol(self):
        self.volume = self.height * self.width * self.deep
        return self.volume

# Test
if __name__ == '__main__':

    width = 5 
    height = 6
    deep = 3
    # Object instance
    cube = Cube(height=height, width=width, deep=deep)

    print('The cube volume is: ')
    print(cube.calc_vol())
    
# %%
