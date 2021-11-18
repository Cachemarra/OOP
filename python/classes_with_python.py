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

# %%
