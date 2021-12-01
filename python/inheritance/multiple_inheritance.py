#%% Multiple inheritance.
# We are going to use the same classes from simple_inheritance code.#%% Creation of a class a achild

# Father class
class SimpleList():

    def __init__(self, elements: list):
        self._elements = elements

    def add(self, element: any):
        self._elements.append(element)

    # Method to sort the list
    def sort(self):
        self._elements.sort()

    # Overload. The method will be called when try to access an item in this notation: []
    def __getitem__(self, index):
        return self._element[index]

    # Overload to get the lenght of the list
    def __len__(self):
        return len(self._elements)

    # Method similar to __str__ but more technically
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elements!r})'


# Creation of the child class
# We want to inherit all methods from father class
class OrderedList(SimpleList):

    def __init__(self, elements = []):
        # We need to call father initiation
        super().__init__(elements)
        # Once init the elements, we order the elements.
        # This metod is inherited from father class.
        self.sort()

    # Overriding a father class
    def add(self, element):
        # Calls father class and extend working
        super().add(element)
        # Sort the elements.
        self.sort()


# New child.
class IntList(SimpleList):
    ''' Child class of SimpleList
    This class operates with lists, but only those with numeric values.
    '''
    def __init__(self, elements: list = []):
        # Check every element to see if are valid.
        for element in elements:
            self._validate(element)
        
        # if are valids, we add it
        super().__init__(elements)

    
    # Validation function
    def _validate(self, element):
        # Validate if are int or not.
        if not isinstance(element, int):
            raise ValueError(f'The value {element} is not int type.')

    # Overloading add class from father class.
    def add(self, element):
        self._validate(element)
        # If is valid, we add it.
        super().add(element)


####################################################
### There's no relationship between orderedlist and intlist.
# We are going to create a child that will have both features.

# The order of declaration is important, it says the importance of inheritance.
class OrderedIntList(IntList, OrderedList):
    # By now, this is enogh to use the new class. but there's no extra features.
    pass



# Test

if __name__ == '__main__':

    # With the basic form using just pass
    ordered_int_list = OrderedIntList([1, 2, 3, 0, -1, -3, 10])
    print(f'ordered int list: {ordered_int_list}')

    # Trying using string
    try:
        ordered_int_list2 = OrderedIntList([1, '2', 3, '0', -1, -3, 10])
    except Exception as err:
        print(err)

    # adding values:
    ordered_int_list.add(7)
    print(f'ordered int list: {ordered_int_list}')

    # Remember, to know which method or father has more weight we can use mro function or __bases__.
    print(OrderedIntList.__bases__)
    # But mro is more deep in the information.
    print(OrderedIntList.__mro__)

