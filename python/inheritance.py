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

# %% Operators override
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
    
    def __init__(self, width: float, height: float, colour: str):
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

# We would need abc module to do this. ABC -> Abstract Base Class
from abc import ABC, abstractmethod # Class and decorator.

# We extend the class ABC on Figure to make it abstact.
class Figure(ABC):
    def __init__(self, height: float, width: float) -> None:
        # Adding validation!
        if self._validate_value(height):
            self._height = height
        else:
            self._height = 0

        if self._validate_value(width):
            self._width = width
        else:
            self._width = 0 

    # Override
    def __str__(self):
        return f'FigureClass: [height: {self._height}, width: {self._width}]'
    
    # Other way to get/set values
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if self._validate_value(width):
            self._width = width
        else:
            print('Value not valid!')

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if self._validate_value(height):
            self._height = height
        else:
            print('Value not valid!')
            
    
    # Abstract method
    @abstractmethod
    # This won't have implementation here, is abstract and child method should implement it.
    def get_area(self):
        pass

    # Validation function
    def _validate_value(self, value: float) -> bool:
        return True if 0 < value < 10 else False


# If we try to create an object of Figure class, it will raise an error.
figure = Figure(5, 5)
'''
TypeError: Can't instantiate abstract class Figure with abstract methods get_area
'''
# %% Now, when we create a child class, it must have defined the abstract class
# If not, an error will be raised.

class Square(Figure):
    
    def __init__(self, width: float, height: float, colour: str) -> None:
        # Who is gonna give his parameters with super()?
        # Super will call the first class, what is? nobody knows.
        # We can use the class name!
        # We are using the father class inside the class
        if height == None:
            height = width
        
        Figure.__init__(self, width, height)

    '''
    def get_area(self):
        # Using the parameters obtained by father class.
        return self.height * self.width
    '''

square = Square(10, 10, 'green')
'''
TypeError: Can't instantiate abstract class Square with abstract methods get_area
'''

# %% Now with the abstract method defined
class Square(Figure):
    
    def __init__(self, width: float, height: float, colour: str) -> None:
        # Who is gonna give his parameters with super()?
        # Super will call the first class, what is? nobody knows.
        # We can use the class name!
        # We are using the father class inside the class
        if height == None:
            height = width
        
        Figure.__init__(self, width, height)

    
    def get_area(self):
        # Using the parameters obtained by father class.
        return self.height * self.width
    

square = Square(5.0, 5.0, 'green')
square.get_area()

# %% Class variables
# A class variable is a variable that is shared by all the objects of the class.
# Each object that modifies that value will change it for all instances.

# A class variable is outside every method.
class MyClass:
    # Class variable
    class_variable = 'class variable value'

    def __init__(self, instance_variable: str) -> None:
        # Instance variable
        self.instance_variable = instance_variable


# to access an class variable, we need to use the class name, there is no need to 
# create an object.
print('class variable'.center(50, '-'))
print(MyClass.class_variable)
print('myclass values'.center(50, '-'))
myclass = MyClass('instance variable value')
print(myclass.instance_variable)
# We can also access with the object
print(myclass.class_variable)

# Another object
print('with another class'.center(40, '-'))
myclass2 = MyClass('instance variable value 2')
print(myclass2.instance_variable)
print(myclass2.class_variable)
# What happened if we change the class variable?
print('change class variable'.center(40, '-'))
myclass.class_variable = 'new class variable value'
print('myclass class variable: ', myclass.class_variable)
print('myclass2 class variable: ', myclass2.class_variable)
# In that case, the class variable will be changed only for that instance.

# %% Class Variables on the flight (OTF)
# We can associate a new class variable in every moment.
# Created on the fly
MyClass.class_variable2 = 'Class variable value 2'

myclass = MyClass('instance variable value')

print('Accessing the new class variable'.center(40, '-'))
print('MyClass: ', MyClass.class_variable2)
print('myclass: ', myclass.class_variable2)

# %% Static methods
# Associated to the class, not to the object. We need use the @staticmethod decorator.

class MyClass:
    class_variable = 'Class variable value'

    def __init__(self, instance_variable: str) -> None:
        # Instance variable
        self.instance_variable = instance_variable

    @staticmethod
    # It doesn't need self. It will be called without the object.
    # An static method CANNOT access the instance variables! nor dinamic state
    def static_method():
        # We can access indirectly the class variable
        print(MyClass.class_variable)


# To call static method we don't need create an object

MyClass.static_method()

# %% Class methods
# Class methods and static methods don't receive info from the class, so they're not 
# relationated. We can substitute the method as other function in our module.
# It function is to associate a function to the class.
# Remember, static method don't receive class info itself.

# In other hand, class method requires the decorator @classmethod.
# They will have some info from the class

class MyClass:
    class_variable = 'Class variable value'

    def __init__(self, instance_variable: str) -> None:
        # Instance variable
        self.instance_variable = instance_variable

    @staticmethod
    # It doesn't need self. It will be called without the object.
    # An static method CANNOT access the instance variables! nor dinamic state
    def static_method():
        # We can access indirectly the class variable
        print('static method')
        print(MyClass.class_variable)

    @classmethod
    def class_method(cls): # cls is the class name, it's the standar name.
        # We can access indirectly the class variable
        print('class_method')
        print(cls.class_variable) # cls points to the class.

    # dynamic method
    def instance_method(self):
        print('instance_method')
        self.class_method()
        self.static_method()
        print(self.instance_variable)
        print(self.class_variable)

MyClass.class_method() # it pass self as cls directly.

# Note. A static context can't access dinamic context, but dynamic context can access
# a static context.
myclasss = MyClass('instance variable value')
myclasss.class_method()
print('dynamic method'.center(40, '-'))
myclasss.instance_method()

# %% Aggregates
# File Prac3.py
