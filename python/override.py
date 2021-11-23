#%% Operators Overloading!
# An operator can change the behavior depends on the object.
# E.g. a string plus a string is concatenation.
# But a string plus a number is addition.
# Finally, a number plus a number is addition.
# Another example is multiplication.
# You can't multiply string * string, but you can multiply string * number.
# or number * number.

# Most common operands and their methods:
'''
__add__(self, other) ->         '+' ->  addition
__sub__(self, other) ->         '-' ->  subtraction
__mul__(self, other) ->         '*' ->  multiplication
__truediv__(self, other) ->     '/' ->  division
__floordiv__(self, other) ->    '//' -> floor division
__mod__(self, other) ->         '%' ->  modulo
__pow__(self, other) ->         '**' -> power
'''

# Operator Overloading
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    # This operator is called automatically always you use + operator with two Person classes
    def __add__(self, other):
        return self.name + ' & ' + other.name

    def __sub__(self, other):
        return self.age - other.age


if __name__ == '__main__':
    p1 = Person('John', 20)
    p2 = Person('Mary', 30)
    print(p1 + p2)
    print(p1 - p2)
# %%
