#%% Creation of a class a achild
# 
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





# Test

if __name__ == '__main__':

    simple_list = SimpleList([1, 2, 3, 0, -1, -3, 10])
    print(f'simple list: {simple_list}')

    # Test child class
    ordered_list = OrderedList([1, 2, 3, 0, -1, -3, 10])
    print(f'Ordered list: {ordered_list}')

    # Adding elements and printing
    print()

    simple_list.add(-5)
    ordered_list.add(-5)

    print(f'simple list: {simple_list}')
    print(f'Ordered list: {ordered_list}\n')

    # Testing IntList
    try:
        #                                  str values
        intlist = IntList([1, 5, 4, 0, 34, '1', '3'])
    except Exception as err:
        print(err)

    intlist = IntList([1, 4, -1, -9, 3])

    print(f'intlist: {intlist}')