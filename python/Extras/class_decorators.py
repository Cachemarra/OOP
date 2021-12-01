#%% Class decorators

import inspect # To get the signature.

# Allow us to transsform our class.
# The operation is similar to functions decorators.

# Creating the decorator
def decorator_repr(cls):
    print('Decorator Executed')
    print(f"Receiving object class: {cls.__name__}")

    # Check class attributes with vars method
    attributes = vars(cls)

    # Check every attribute
    for name, attribute in attributes.items():
        print(f'name: {name}, attribute: {attribute}')
    # This will show us the property methods but not the self._ 

    # Check if __init__ method has not been overwritted
    # I mean, If the class has not his own __init__ method.
    if '__init__' not in attributes:
        raise TypeError(f'{cls.__name__} no overriding __init__ method.') 

    # Getting the signature of __init__ method with inspect
    init_signature = inspect.signature(cls.__init__)
    print(f'Init signature: {init_signature}')

    # Getting parameters except 'self'

    parameters_init = list(init_signature.parameters)[1:] # To skip the first element.
    print(f'Init parameters: {parameters_init}')

    # Check if each parameter has his own property method,it is, is encapsulated.
    for parameter in parameters_init:
        # Check if the method (shoul have the same name) is property type
        is_property_method = isinstance(attributes.get(parameter), property)

        if not is_property_method:
            raise TypeError(f"There's no property method for the attribute {parameter}")


    # Creation of __repr__ method dynamically
    # Is an instance method, that's why it needs 'self'
    def repr_method(self):
        # Getting class name
        class_name = self.__class__.__name__

        print(f'Class name: {class_name}')

        # Getting property names and his values
        # We're gonna use a generator expression.
        # It will create a string with name and attribute name: atr_name = atr_value
                            # yield
        arg_generator = (f'{name} = {getattr(self, name)!r}' 
        for name in parameters_init) # Generator.

        # Casting to list
        arg_list = list(arg_generator)
        print(f'Generator List: {arg_list}')

        # Repr returns a string, so casting to string..
        arguments = ', '.join(arg_list)
        print(f'Repr arguments: {arguments}')

        # Create repr method without using his name
        repr_result = f'{class_name}({arguments})'

        return repr_result
        



    # Adding repr method to our class
    setattr(cls, '__repr__', repr_method)




    return cls # If not returned, an error will be raised


# Creation of a class
@decorator_repr # Calling decorator.
class Person:
    def __init__(self, first_name, last_name) -> None:
        print('Constructor executed')
        self._first_name = first_name
        self._last_name = last_name

    # Encapsulation
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __repr__(self):
        return f'Person({self._first_name, {self._last_name}})'



# Creating object
person = Person('John', 'Doe')
print(person)

