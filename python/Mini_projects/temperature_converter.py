#%% Create a class that can convert from Cº to Fº and Fª -> Cº

# Creating class

class temperature_converter:
    # Class parameters
    # Constanst of max values.
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 123

    # the conversion rate is C * (9/5) + 32
    @classmethod
    def celsius_to_fahrenheit(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'[ERROR] Very high temperature: {celsius}. Max permited is {cls.MAX_CELSIUS}')
        # Else return the convertion
        return celsius * (9/5) + 32
    

    # Fahrenheit to Celsius
    @classmethod
    def fahrenheit_to_celsius(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'[ERROR] Very high temperature: {fahrenheit}. Max permited is {cls.MAX_FAHRENHEIT}')
        # Else return the convertion
        return (fahrenheit - 32) * (5/9)


if __name__ == '__main__':
    celsius = 30
    fahrenheit = 0

    ans1 = temperature_converter.celsius_to_fahrenheit(celsius=celsius)
    ans2 = temperature_converter.fahrenheit_to_celsius(fahrenheit)

    print('First test'.center(45, '-'))
    print(f'Celsius to Fahrenheit. {celsius} ºC are {ans1} ºF')
    print(f'Fahrenheit to Celsius. {fahrenheit} ºF are {ans2} ºC\n')

    # Second test
    celsius = 120
    fahrenheit = 150

    print('Second test'.center(45, '-'))
    try:
        ans1 = temperature_converter.celsius_to_fahrenheit(celsius=celsius)
        print(f'Celsius to Fahrenheit. {celsius} ºC are {ans1} ºF')
    except Exception as err:
        print(err)
    
    try:
        ans2 = temperature_converter.fahrenheit_to_celsius(fahrenheit)
        print(f'Fahrenheit to Celsius. {fahrenheit} ºF are {ans2} ºC')
    except Exception as err:
        print(err)




# %%
