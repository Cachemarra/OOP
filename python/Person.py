#%% Final class
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

    # Destructor Class
    def __del__(self):
        print(f'Person: {self._first_name}, {self._last_name}')


    # Method Override!
    # If we call a print(Person) it will return a string and show this values.
    def __str__(self) -> str:
            return f'PersonClass[{self._first_name}, {self._last_name}, {self._age}]'
    

#%% Above this line is the topic of Inheritance!

class Employee(Person):
    def __init__(self, first_name, last_name, age, salary):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        pass

    # Overriding father method
    def __str__(self):
        # We return the same values of father __str__ + salary.
        return f'EmployeeClass[Salary: {self.salary} ]{super().__str__()}'


