#%% Polymorphism in python
# A class can have multiple methods with the same name but different signatures.
# This is called polymorphism.
# Execute multiple methods depends on the class.

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: [Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager: [Department: {self.department}], {super().__str__()}"



# Trying Polymorphism
def print_details(object):
    # Calls the __str__ method of the object
    print(object)
    # Check what kind of object is
    print(type(object))

    # If we want to access department attribute. We just can access if is Manager
    if isinstance(object, Manager):
        print(object.department)


Employee = Employee("John", 10000)
Manager = Manager("John", 10000, "IT")

print('Employee'.center(50, '-'))
print_details(Employee)
print('Manager'.center(50, '-'))
print_details(Manager)


# %%
