'''
Practice with objects trying to apply everything I have learned so far.

There are going to be 6 objects: Computer, Monitor, Order, InputDevice, Mouse, Keyboard.
Note: Computer can be added to Order.
Keyboard and Mouse are going to be added to InputDevice.
Monitor is going to be added to Computer.
Mouse and keyboard are child of InputDevice.

The final output comes from the Order object.

Computer:
    Parameters: 
        ComputerCount: int <<static>>
        ComputerID: int
        name: str
        monitor: Monitor
        keyboard: Keyboard
        mouse: Mouse
    Methods:
        __str__
        Setters and Getters to each attribute
    Responsabilities:
        Create Computer objects

Order:
    Parameters:
        OrderCount: int <<static>>
        OrderID: int
    Methods:
        addComputer(Computer)
        __str__
        setter and getters
    Responsabilities:
        Create Order objects and store a list of 
        computer objects.

Monitor:
    Parameters:
        MonitorCount: int <<static>>
        MonitorID: int
        brand: str
        size: int
    Methods:
        __str__
        setter and getters
    Responsabilities:
        Create Monitor objects

InputDevice:
    Parameters:
        InputType: str
        brand: str
    Methods:
        __str__
        setter and getters
    Responsabilities:
        Create InputDevice objects

Mouse:
    Parameters: 
        MouseCount: int <<static>>
        MouseID: int
    Methods:
        __str__
    Responsabilities:
        Create Mouse objects
    
Keyboard:
    Parameters:
        KeyboardCount: int <<static>>
        KeyboardID: int
    Methods:
        __str__
    Responsabilities:
        Create Keyboard objects

'''
# Order class
class Order:

    pass


# Computer class
class Computer:
    pass


# Monitor class
class Monitor:
    pass


#InputDevice class
class InputDevice:
    """
    Class parent for Mouse and Keyboard.
    """

    def __init__(self, inputType:str, brand: str) -> None:
        self._inputType = inputType
        self._brand = brand

    # Methods
    def __str__(self) -> str:
        return f'Brand: {self._brand}, InputType: {self._inputType}'
    
    # Setters and Getters
    @property
    def inputType(self) -> str:
        return self._inputType
    
    @inputType.setter
    def inputType(self, inputType: str) -> None:
        self._inputType = inputType
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @brand.setter
    def brand(self, brand: str) -> None:
        self._brand = brand


# Child class of InputDevice
# Mouse class
class Mouse(InputDevice):
    """
    Class to define Mouse devices as Input Device.
    """
    # Static attributes
    MouseCount = 0

    def __input__(self, mouseID: int) -> None:
        self._mouseID = mouseID
        increaseMouseCount()
        self._mouseCount = Mouse.MouseCount


    # Method to increase the static attribute MouseCount
    @staticmethod
    def increaseMouseCount() -> None:
        Mouse.MouseCount += 1
    


# Keyboard class
class Keyboard:
    pass













