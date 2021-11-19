#%% Inheritance with python
# Import the father class
from Person import Person

#%% Employee class.
# We are going to create a class Employee who is a children of Person class.
# Not all Persons are employees nor have a salary.
# To indicate is a children we must define the father class

class Employee(Person): # Inheritance of Person class.
    # Constructor
    def __init__(self, first_name, last_name, age, salary):
        # To have the same parameters as Person we should use "super()"
        # This will call the contructor of father class
        super().__init__(first_name, last_name, age)
        self.salary = salary

# Creating a Employee object
#  This will raise an error, we must pass the parameters of Person too!
#person1 = Employee(5_000)
person1 = Employee('Juan', 'Gomez', 25, 5_000)
# We can also use father methods!
person1.show_details()
print(f'Salary: {person1.salary}')


# %% Multiple Inheritance
# We are going to create two father classes, Figure and Colour.
# Both will have a child called Square, which will inherit both classes.
# Figure will have Width and Height parameters, Colour will have just colour parameter
# For commodity, The three classes will be in Person.py.
# Father Classes
class Figure:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


class Colour:
    def __init__(self, colour: str) -> None: 
        self.colour = colour


# Child class with 2 parents
class Square(Figure, Colour):
    
    def __init__(self, width: float, height: float, colour: str) -> None:
        # Who is gonna give his parameters with super()?
        # Super will call the first class, what is? nobody knows.
        # We can use the class name!
        # We are using the father class inside the class
        if height == None:
            height = width
        
        Figure.__init__(self, width, height)
        Colour.__init__(self, colour)

    def get_area(self):
        # Using the parameters obtained by father class.
        return self.height * self.width

square = Square(10, 10, 'green')
print(f'Area = {square.get_area()}')
print(f'Colour = {square.colour}')

# %% Practic2.py exercise!
#####
#####
# %% Method Resolution Order (MRO)
# To know how the order hierarchy of father classes
Square.mro()
# [__main__.Square, __main__.Figure, __main__.Colour, object]
# That means that it first call Square, then Figure, Colour and lastly, Object.
# Every method call will search in the order that MRO gives

# %% New practice at practic2.py
## Creation of two classes with multiple inheritance.
######################

#%% Abstraction.
# It doesn't have implementation in father class but in children classes.
# There are necessary in children classes. If we create an abstract method,
# ALL the class turns into an abstract class, meaning we can not longer instanciate ir nor
# create objects with it, just inherit.
