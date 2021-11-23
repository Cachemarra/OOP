#%% 
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


Example Output:
Order 1, Computers:
    HP: 1
        Monitor: ID: 1, brand: Hp, size: 15inch
        Keyboard: ID: 1, brand: Hp, input_type: usb
        Mouse: ID: 1, brand: Hp, input_type:  usb

    Acer: 2
        Monitor: ID: 2, brand: Acer, size: 27inch
        Keyboard: ID: 2, brand: Acer, input_type: Bluetooth
        Mouse: ID: 2, brand: Acer, input_type:  Bluetooth

'''
# Order class
class Order:
    """
    Final class. It will store all other classes
    """

    orderCount = 0

    def __init__(self):
        Order.orderCount += 1
        self._orderID = Order.orderCount
        self._computerList = []

    def __str__(self):
        text1 = f'Order {self._orderID}, Computers: \n'
        texts = ''
        for computers in self._computerList:
            texts += '\t' + computers.__str__() + '\n'
        
        return text1 + texts

    def agg_computer(self, computer: Computer):
        self._computerList.append(computer)

    @property
    def orderID(self):
        return self._orderID

    @orderID.setter
    def orderID(self, order: int):
        self._orderID = order
    


# Computer class
class Computer:
    """
    It must have aggregation method for Monitors, keyboard and mouse.
    """
    computerCount = 0

    def __init__(self, name: str, monitor: Monitor, keyboard: Keyboard, mouse: Mouse):
        Computer.computerCount += 1
        self._computerID = Computer.computerCount
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    
    def __str__(self):
        text1 = f'{self._name}: {self._computerID} \n'
        text2 = '\t' + self._monitor.__str__() + '\n'
        text3 = '\t' + self._keyboard.__str__() + '\n'
        text4 = '\t' + self._mouse.__str__() + '\n'

        return text1 + text2 + text3 + text4

    # Getter and setter
    @property
    def computerID(self):
        return self._computerID
    
    @property
    def name(self):
        return self._name
    
    @property
    def monitor(self):
        return self._monitor.__str__()
    
    @property
    def keyboard(self):
        return self._keyboard.__str__()
    
    @property
    def mouse(self):
        return self._mouse.__str__()


    @computerID.setter
    def computerID(self, value: int):
        self._computerID = value
    
    @name.setter
    def name(self, value:str):
        self._name = value
    
    @monitor.setter
    def monitor(self, monitor: Monitor):
        self._monitor = monitor

    @keyboard.setter
    def keyboard(self, keyboard: Keyboard):
        self._keyboard = keyboard
    
    @mouse.setter
    def mouse(self, mouse: Mouse):
        self._mouse = mouse


# Monitor class
class Monitor:
    monitorCount = 0

    def __init__(self, brand: str, size: float):
        Monitor.monitorCount += 1
        self._monitorID = Monitor.monitorCount
        self._brand = brand
        self._size = size

    def __str__(self):
        return f'Monitor: ID: {self._monitorID}, brand: {self._brand}, size: {self._size} inches.'

    # Setter and getter
    @property
    def monitorID(self) -> int:
        return self._monitorID

    @monitorID.setter
    def monitorID(self, value: int) -> None:
        self._monitorID = value

    @property
    def brand(self) -> str:
        return self._brand
    
    @brand.setter
    def brand(self, value: str) -> None:
        self._brand = value

    @property
    def size(self) -> None:
        return self._size

    @size.setter
    def size(self, value: float) -> None:
        self._size = value


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

    def __init__(self, input_type: str, brand: str) -> None:
        Mouse.MouseCount += 1
        self._mouseID = Mouse.MouseCount
        super().__init__(inputType=input_type, brand=brand)


    def __str__(self) -> str:
        return f'Mouse: ID: {self._mouseID},  {super().__str__()}'


# Keyboard class
class Keyboard(InputDevice):
    """
    Class to define Keyboard devices as Input Device.
    """
    # Static attributes
    KeyboardCount = 0

    def __init__(self, input_type: str, brand: str) -> None:
        Keyboard.KeyboardCount += 1
        self._keyboardID = Keyboard.KeyboardCount
        super().__init__(inputType=input_type, brand=brand)


    def __str__(self) -> str:
        return f'Keyboard: ID: {self._keyboardID}, {super().__str__()}'


###############################
#%%
if __name__ == '__main__':

    mouse = Mouse('Bluetooth', 'Asus')
    mouse2 = Mouse('Wired', 'Corsair')

    print('Mouses'.center(40, '-'))
    print('Mouse 1')
    print(mouse)
    print('Mouse 2')
    print(mouse2)

    keyboard = Keyboard('Bluetooth', 'Aorus')
    keyborad2 = Keyboard('Wired', 'ROG Strix')

    print('Keyboard'.center(40, '-'))
    print('Keyboard 1')
    print(keyboard)
    print('Keyboard 2')
    print(keyborad2)

    monitor = Monitor('Asus', 26)
    monitor2 = Monitor('Aorus', 23)
    print('Monitor'.center(40, '-'))
    print('monitor 1')
    print(monitor)
    print('monitor 2')
    print(monitor2)

    computer = Computer('First PC', monitor, keyboard, mouse)
    computer2 = Computer('Second PC', monitor=monitor2, keyboard=keyborad2, mouse=mouse2)
    print('Computer'.center(40, '-'))
    print('Computer 1')
    print(computer)
    print('Computer 2')
    print(computer2)

    order = Order()
    order.agg_computer(computer)
    order.agg_computer(computer2)
    print('Order'.center(40, '-'))
    print('Order----------')
    print(order)
 

# %%
