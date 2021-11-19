#%% Object Oriented Programming in python

# Creation of an empty class
from typing import AsyncGenerator


class Person:
    pass

# Check the type
print(type(Person))
# %%
# Creation of a class and his constructor with __init__
# if not defined, python would create it in background
# Default parameter is self, like "this" in C++
# The pre and pos __ means that is private(pre) and (pos)
# the __var__ is called dunder

# Also add attributes of instance with self, meaning that is part of the class
# We define default parameters. NOTE: this is not the best way to assign default values.
class Person:

    def __init__(self):
        self.first_name = 'Juan'
        self.last_name = 'Perez'
        self.age = 28

# Checking the parameters of our class
person1 = Person() # <- Call to class construction who calls __init__
print(person1.first_name) # <- We access to the parameter with dot '.' function.
print(person1.last_name)
print(person1.age) 
#%% Adding parameters to init
# This is the common way to assign values to attributes
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Now we have to pass the values of each parameter!
# Person(first_name = 'Juan', last_name = 'Perez', age=28)
person1 = Person('Juan', 'Perez', 28) # <- Call to class construction who calls __init__

print(person1.first_name)
print(person1.last_name)
print(person1.age) 

#%% We can create multiple instances of the same class

person2 = Person('Karla', 'Ramirez', 18)
print('Person 2 values:')
print(person2.first_name)
print(person2.last_name)
print(person2.age) 

print('\nPerson 1 values:')
print(person1.first_name)
print(person1.last_name)
print(person1.age) 

# %% Modify parameters
# We can modify the parameters with a simple assignation
person1.first_name = 'Eli'
person1.last_name = 'Gomez'
person1.age = 42

print(person1.first_name)
print(person1.last_name)
print(person1.age) 

# %% add a method called show_details

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # New method
    def show_details(self):
        print(f'person: {self.first_name}')
        print(f'last name: {self.last_name}')
        print(f'age: {self.age}')

# We can use the new method with each object of the Person class.
person1 = Person('Juan', 'Perez', 25)
person1.show_details()

# We can also use the method passing the reference of the object
print('\nUsing method with the object reference')
Person.show_details(person1)

# %% We can create attributes on the fly.
person1.telephone = '555-555-507'
print(person1.telephone)

# But it will not be share with other objects, is unique of person1!
# This will raise an AttributeError!
print(person2.telephone)

#%%#####################################%%
####### Check pract1.py     #############
#########################################
#%% Expanding __init__
# To pass a variable toupe we sould use *args 
# To pass a dictionary of data use **kwargs

class Person:
    def __init__(self, first_name, last_name, age, *args, **kwargs) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        self.args = args
        self.kwargs = kwargs
    
    # New method
    def show_details(self):
        print(f'person: {self.first_name}')
        print(f'last name: {self.last_name}')
        print(f'age: {self.age}')
        print(f'args: {self.args}')
        print(f'kwargs : {self.kwargs}')


# Now we can pass more arguments, even if there are not defined
#                                     *args--------------- **kwargs-------------------
person1 = Person('Juan', 'Perez', 28, '555-156', 1, 34, 5, name='hello', other='world')

person1.show_details()


# %% Encapsulation
# The attributes 'first_name', 'last_name', 'age' are PUBLIC attributes and we can access
# and modifying directly. If we want to declare that the attribute is private we should add a '_' prefix
# in other languages it prevents the modification, but in python is just an advice to the programmer.
# If we use '__' the attribute can't be accessed nor modified out of the class.
class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self._first_name = first_name # Encapsulated
        self.__last_name = last_name
        self.age = age

    # We can acces creating a decorator method, modifying the function as if
    # it were an attribute instead a method.
    @property
    def first_name(self):
        # To check if we are calling it
        print('Calling first decorator')
        return self._first_name

    # Setter method to modify _first_name attribute
    @first_name.setter
    def first_name(self, first_name):
        print('Calling second decorator')
        self._first_name = first_name


person1 = Person('Juan', 'Perez', 28)
person1._first_name = 'Otto' # <- We can modify the attribute, but if it has an '_' we shouldn't touch it.

print(person1._first_name)
person1.__last_name = 'Ramirez'
print(person1.__last_name)
# Checking the attribute with decorator
print(person1.first_name)

# Changing the name with the decorator setter
person1.first_name = 'Juan Alberto'

print(person1.first_name)
# %% Read-Only attributes

# If we comment this line of the class
# The attribute can't be modified unless it is accessed as _first_name
@first_name.setter
def first_name(self, first_name):
    print('Calling second decorator')
    self._first_name = first_name


#%% Encapsulating all attributes

class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self._first_name = first_name # Encapsulated
        self._last_name = last_name
        self._age = age

    # We can acces creating a decorator method, modifying the function as if
    # it were an attribute instead a method.
    @property
    def first_name(self):
        # To check if we are calling it
        return self._first_name

    # Setter method to modify _first_name attribute
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    # New method
    def show_details(self):
        # We can acces to private parameters because we are inside the class.
        print(f'person: {self._first_name}')
        print(f'last name: {self._last_name}')
        print(f'age: {self._age}')


# We try the read-only parameters
person1 = Person('Juan', 'Perez', 28)

# Changing the name with the decorator setter
person1.first_name = 'Juan Alberto'
person1.last_name = 'Gomez'
person1.age = 25

person1.show_details()

# %% Creation of a module with the class person
# A file called Person will have the class and constructions
## The file will be called person_test.py ###
##########################################################

#%% Destructors

class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self._first_name = first_name # Encapsulated
        self._last_name = last_name
        self._age = age

    # We can acces creating a decorator method, modifying the function as if
    # it were an attribute instead a method.
    @property
    def first_name(self):
        # To check if we are calling it
        return self._first_name

    # Setter method to modify _first_name attribute
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    # New method
    def show_details(self):
        # We can acces to private parameters because we are inside the class.
        print(f'person: {self._first_name}')
        print(f'last name: {self._last_name}')
        print(f'age: {self._age}')

    # Method inherit from object class
    # All clases are children of object class
    def __del__(self):
        print(f'Person: {self._first_name}, {self._last_name}')


person1 = Person

print('Creation'.center(40, '-'))
person1 = Person('Juan', 'Perez', 28)

# We rarely delete objects explicit. The Python Garbage collector automatically
# deletes objects without a variable or if the script ends.
print('Deletion'.center(40, '-'))
del person1

