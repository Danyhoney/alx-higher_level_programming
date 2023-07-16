#!/usr/bin/python3

"""
File_name: 3-square.py
Created: 30th of May, 2023
Auth: Daniel Nyong (Danyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
"""


class Square:

    """
    # Write a class Square that defines a square by: (based on 2-square.py)
    # Private instance attribute: size
    # Instantiation with optional size: def __init__(self, size=0):
    # VARIABLE(" "):
    # class(Square): Area of a square
    # Return: Always 0. (Success)
    """
    """ the '__init __' method takes an optional parameter 'size', with...
    a default value of 0. it will perform the below checks..."""
    def __init__(self, size=0):
        """ If the 'size' is not an instance of 'int', it raises a 'TypeError
        ...Exception with the message 'Size Must Be An Integer' """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            """If the size is less than '0', it raises a 'ValueError'
            Exception with the message, 'size must be >= 0'"""
            """Otherwise, it assigns the provided 'size' value to the Private
            ...Instance attribute '__size'"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Here, a public instance method 'area()' is defined. This method..
        calculates and return the area of the square by multiplying...
        the '__size' attribute by itself..."""
        return self.__size ** 2
