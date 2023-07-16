#!/usr/bin/python3

"""
File_name: 1-square.py
Created: 30th of May, 2023
Auth: Daniel Nyong (Danyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
"""


class Square:

    """
    # Write a class Square that defines a square by: (based on 0-square.py)
    # Private instance attribute: size
    # Instantiation with size (no type/value verification)
    # VARIABLE(" "):
    # class(Square): Square with size
    # Return: Always 0. (Success)
    """
    """ Here, the '__init__' method is used as the constructor."""
    def __init__(self, size):
        """ It takes a parameter 'size' and initializes the private instance...
        ...attribute '__size' with the provided value"""
        self.__size = size
