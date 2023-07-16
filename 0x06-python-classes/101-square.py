#!/usr/bin/python3
"""Python Module(Squares)
"""
'''
File_name: 101-square.py
Created: 30th of May, 2023
Auth: Daniel Nyong (Danyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
'''


class Square:
    '''Constructor (__init__ method):
    The __init__ method is the constructor of the class. It takes two
     optional parameters: size (defaulting to 0) and position....
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''...efaulting to (0, 0)). It assigns the values of size and position
        ...to the respective attributes using the setter methods.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Size property:
        The size property allows getting and setting the size attribute of the
        Square class.The getter method simply returns the value of self.__size
        The setter method performs type and value checks. It raises a
        ...TypeError if the value is not an integer and a ValueError if the..
        value is less than 0. Otherwise, it assigns the value to self.__size'''
        return self.__size

    @property
    def position(self):
        '''Retrieves and exact position and returns tuple
        '''
        return self.__position

    @size.setter
    def size(self, value):
        '''Updating the size of Square.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        '''Retrieves and exact position and returns tuple
        '''
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        '''Calculating the area of square
        '''
        return self.size ** 2

    def my_print(self):
        '''Printing a 2D table '#' with symbol and size of exact
        square position...
        '''
        if self.size == 0:
            print('\n')
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.size))

    def __str__(self):
        '''returns a string
        '''
        strings = []
        if self.size == 0:
            strings.append('')
        else:
            if self.position[1] > 0:
                strings.append('{}'.format('\n' * (self.position[1] - 1)))
            for i in range(self.size):
                strings.append('{}{}'.format(
                    ' ' * self.position[0],
                    '#' * self.size))
        return '\n'.join(strings)
