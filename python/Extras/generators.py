#%% Generator
# A generator returns a sequence of values by the 'yield' command.
# It's not necessary to use return when using a generator.
# It's a special function.
# The main feature is that the generator, unlike the function, pauses it instead
# of stoping.

# It returns on demand!
def generator():
    yield 1
    yield 2
    yield 3


# Using generator
gen = generator()

# By 'next' we call every yield
print('gen value: ', next(gen))

# testing
print('loop'.center(45, '-'))
for i in range(2):
    print('gen value: ', next(gen))

# Note that in the loop it starts with the second yield.
# If there's no more items in yield, the generator will raise an "StopIteration" error.

# We can also iterate over generator.
print('Iterating over generator()'.center(45, '-'))
for i in generator():
    print('Generator number: ', i)

    
# %% Example with generators.
# Generator of numbers 1 -> 5

def number_generator():
    for number in range(1, 6):
        yield number
        print('Continue generating') # To ilustrate that the gen continue from previous call.

# Using the generator
generator = number_generator()

print('General data'.center(45, '-'))
print(f'Generator Object: {generator}')
print(type(generator))

# Using generator:
for value in generator:
    print(f'Generate number: {value}')
    
# We don't have more values to generate, so we will call it again.
generator = number_generator()
print(f'\nOn-demand generating: {next(generator)}')



# %% Expression generator.
# Anonymous generator.

# The syntaxis is similar to list comprehension.
       # Yield      # Generator.
mult = (value*value for value in range(4))

# Check if is generator
print(type(mult))

# Checking values:
print(next(mult))
print(next(mult))
print(next(mult))
print(next(mult))

# %% You can pass a generator to a function.
# If that's the case, you omit '()'
# Passing the generator to a function.
add = sum((val*val for val in range(4)))

print(f'Add result: {add}')

#%% List Generators.

lists = ['Foo', 'Doe']

# We are not generating perse but retrieving.
generator = (value for value in lists)

print(next(generator))
print(next(generator))

# %% string creation by generators using list.
lists = ['John', 'Travolta']

counter = 0

# creating a function to increase counter
def increase():
    global counter
    counter += 1
    return counter


# Creating generator var
#               ----- yield ------
generator = (f'{increase()}. {name}' for name in lists)
lists = list(generator)

# The new list with the modified names.
print(lists)



