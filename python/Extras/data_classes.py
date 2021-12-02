#%% Use of dataclasses
# Dataclasses is a library who help us to create class methods
# dynamically like __init__(), __repr__() ect.
# This script is a brief introduction to dataclasses.

# Import dataclasses
from dataclasses import dataclass
from typing import ClassVar

# We can add __eq__ configuring in the dataclass
@dataclass(eq=True, frozen=True)
class Person:
    # We have to define our variables and data types
    first_name: str
    last_name: str
    # This is all dataclass need to create __init__ and __repr__ methods
    # Class attribnutes. We will need import typing -> ClassVar
    person_counter: ClassVar[int] = 0

    # If we don't want empty people were created we use a post_init mehod
    # This allow us to modify the init of our class
    def __post_init__(self):
        if not self.first_name:
            raise ValueError(f'First Name is empty: {self.first_name}')
        



person1 = Person('John', 'Foo')
# Print __str__
print(person1)
# print repr
print(f'{person1!r}')
# Class Variable
print(f'Class variable: {Person.person_counter}')
# Instance variables
print(f'Instance Variables: {person1.__dict__}')

# Variable with empty values
# WWithout the __post_init__ this will be correct.
'''
empty_person = Person('', '')
printf(f'Empty Person: {empty_person}')
'''

# Checking equality between objects
person2 = Person('Juana', 'DeArco')
print(f'Equal objects? {person1 == person2}')

# We can create inmmutable classes by writing 'frozen' In the decorator.

collection = {person1, person2}
print(collection)

# collection[0].firstname = 'Louis' # This will raise an error as the class is now inmutable.


#%% Relationating classes
# A new class Addres

@dataclass(eq=True, frozen=True)
class Address:
    street: str
    number: int = 0

# Recreating the class
@dataclass(eq=True, frozen=True)
class Person:
    first_name: str
    last_name: str
    person_counter: ClassVar[int] = 0
    address: Address

    def __post_init__(self):
        if not self.first_name:
            raise ValueError(f'First Name is empty: {self.first_name}')


address1 = Address('Palo Alto', 123)
person1 = Person('John', 'Deere', address1)

print(person1)

address2 = Address('Santa Clara', 321)
person2 = Person('Alfred', 'Hg', address2)

# We will check if both have the same content
print(f'Equal objects? {person1 == person2}')

