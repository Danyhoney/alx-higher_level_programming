#!/usr/bin/python3

"""
File_name: 6-square.py
Created: 30th of May, 2023
Auth: Daniel Nyong (Danyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
"""


class Square:

    """
    # Write a class Square that defines a square by: (based on 5-square.py)
    # Private instance attribute: size
    # property def size(self): to retrieve it....
    # property setter def size(self, value): to set it:
    # VARIABLE(" "):
    # class(Square): Coordinates of a square
    # Return: Always 0. (Success)
    """
    """This implementation ensures that the 'size' attribute is an...
    ...integer greater than or equal to zero, and the 'position'"""
    """ attribute is a tuple of two positive integers"""
    """a default value of 0. it will perform the below checks..."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ decorator is used to define a getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """ decorator is used to define a setter method"""
        """If the 'position' isn't an instance of 'int',it raises a 'TypeError
        ...Exception with the message 'Size Must Be An Tuple' """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) and num >= 0 for num in value):
            """If the size is less than '0', it raises a 'ValueError'
            Exception with the message, 'size must be >= 0'"""
            """Otherwise, it assigns the provided 'size' value to the Private
            ...Instance attribute '__size'"""
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Here, a public instance method 'area()' is defined. This method..
        calculates and return the area of the square by multiplying...
        the '__size' attribute by itself..."""
        return self.__size ** 2

    def my_print(self):
        """a new method 'my_print' is introduced"""
        """This method prints a square using the character '#' based on.....
        ...the size of the square"""
        if self.__size == 0:
            """if the suze is 0, it prints an empty line"""
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
