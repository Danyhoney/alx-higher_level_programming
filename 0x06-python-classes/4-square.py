#!/usr/bin/python3

"""
File_name: 4-square.py
Created: 30th of May, 2023
Auth: Daniel Nyong (Danyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
"""


class Square:

    """
    # Write a class Square that defines a square by: (based on 3-square.py)
    # Private instance attribute: size
    # property def size(self): to retrieve it....
    # property setter def size(self, value): to set it:
    # VARIABLE(" "):
    # class(Square): Access and update private attribute
    # Return: Always 0. (Success)
    """
    """ In this version, ther 'square' class introduce propertie...
    ...for the private instance attribute '__size'"""
    """ the '__init __' method takes an optional parameter 'size', with...
    a default value of 0. it will perform the below checks..."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ decorator is used to define a getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """ decorator is used to define a setter method"""
        """ If the 'size' is not an instance of 'int', it raises a 'TypeError
        ...Exception with the message 'Size Must Be An Integer' """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            """If the size is less than '0', it raises a 'ValueError'
            Exception with the message, 'size must be >= 0'"""
            """Otherwise, it assigns the provided 'size' value to the Private
            ...Instance attribute '__size'"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Here, a public instance method 'area()' is defined. This method..
        calculates and return the area of the square by multiplying...
        the '__size' attribute by itself..."""
        return self.__size ** 2
