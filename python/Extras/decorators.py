#%% A brief introduction to decorators in python.
# A decorator is a function whose argument is a function and returns another function.
# It is used for functionality extensions.
# There's needed 3 funcions:
# 1.- Decorator -> A
# 2.- Funtion to decorate -> B
# 3.- Decorated function -> C
# That is:
# function A(B) -> C
# With decorators we can add features after and before execution of the main function.
# To call a decorator you must use '@' char.

#%% Basic decorator

# Decorator definition
def decorator_function_A(function_to_decorate):
    # There's must be a function inside
    def decorated_function_C():
        # We can add code as we wish to be executed before the function calling
        print('Before show_message function'.center(45, '-'))

        # We can use the function_to_decorate without passing as argument for the 'closure' thing.
        function_to_decorate() # If we comment this line nothing will be printed on screen, even when we call "show_message"

        print('After show_message function'.center(45, '-'))

    # We return the function
    return decorated_function_C


@decorator_function_A # <- Who is going to decorate
def show_message():
    print('Hello World from "show_message" fucntion.')


show_message()

# Adding a \n
print('')

# Testing with other function
@decorator_function_A
def prints():
    print('New function called prints.')

prints()

''' Output
---------Before show_message function--------
Hello World from "show_message" fucntion.
---------After show_message function---------

---------Before show_message function--------
New function called prints.
---------After show_message function---------
'''

#%% A decorater can have other parameters

# Decorator definition
def decorator_function_A(function_to_decorate):
    # There's must be a function inside
    def decorated_function_C(*args, **kwargs):
        # We can add code as we wish to be executed before the function calling
        print('Before show_message function'.center(45, '-'))

        # We can use the function_to_decorate without passing as argument for the 'closure' thing.
        ans = function_to_decorate(*args, **kwargs) # Passing the parameters to our decorated functions.

        print('After show_message function'.center(45, '-'))

        return ans # <- We need to return the answer.

    # We return the function
    return decorated_function_C


@decorator_function_A
def add(a, b):
    # Adding operations.
    return a + b


ans = add(4, 6)
print(f'Adding result: {ans}')

''' OUTPUT
---------Before show_message function--------
---------After show_message function---------
Adding result: 10
'''


# %%
