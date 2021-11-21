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


    def __init__(self, width: float, height: float, colour: str) -> None:
