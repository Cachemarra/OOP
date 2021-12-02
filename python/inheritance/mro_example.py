#%% checking things with multiple inheritance
# We are going to create mutiple classes who inherits from different parents

class Class1:
    def __init__(self):
        print('Class1.__init__')

    def method(self):
        print('Method Class1')


# First child. -> Simple Inheritance
class Class2(Class1):
    def __init__(self):
        print('Class2.__init__')

    # Override father method
    def method(self):
        print('Method Class 2.')



# Second child. -> Simple Inheritance
class Class3(Class1):
    def __init__(self):
        print('Class3. __init__')
    
    # Overriding father method 
    def method(self):
        print('Method Class 3')

# Third child. -> Multiple Inheritance.
# We're not going to define __init__, it will take it from the first father we define.
class Class4(Class2, Class3):
    # Overriding method from Class2 just because is the first father
    def method(self):
        print('Method Class4')

# %% Test

if __name__ == '__main__':

    # This is gonna call Class2 __init.__
    class4 = Class4()

    # To know who are the parents we wiill use __base__
    print('Clase4 fathers: ', Class4.__bases__)

    # To see all the lineage of the class4 we use mro. This also tell us the order
    # of resolution
    print('Class4 mro: ', Class4.__mro__)

    # Which method will be called when using method()?
    # Teorically will be the one from class4 as it define it.
    # If you comment the method from class4, class2 will be called.
    class4.method()

    # If we also comment method() from Class3, the one from Class1 will be called.
    # Following the order showed by Class4.__mro__
