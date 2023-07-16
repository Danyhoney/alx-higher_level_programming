#!/usr/bin/python3
"""Python Module(Squares)
"""
'''
File_name: 102-square.py
Created: 30th of May, 2023
Auth: Daniel Nyong (DAnyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
'''


class Square:
    """The 'square' class has a private instance attribute '__size'
    which is accessed through the 'size' property.
    Let's talk briefly about Operators.......
    the comparison operators (>, >=, <, <=, ==, !=) are used to compare
    two objects and determine their relative ordering. These operators
    return a Boolean value (True or False) based on the result...
    ....of the comparison.
    """
    def __init__(self, size=0):
        """Here, we initialize square to a given size '0'"""
        self.size = size

    @property
    def size(self):
        """This should retrieve the size of the square and return"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        """ The'area' method calculates and returns the area of the square
        by multiplying the 'size' attribute by itself('self.size ** 2)
        """
        return self.size ** 2

    def __eq__(self, value):
        '''== (equal to): The __eq__ method overloads the == operator.
        It compares the areas of two square objects (self and other)
        using the area() method. It returns True
        if the areas are equal, and False otherwise.
        '''
        if isinstance(value, Square):
            return self.area() == value.area()
        else:
            return False

    def __ne__(self, value):
        '''!= (not equal to): The __ne__ method overloads the != operator
         It compares the areas of two square objects (self and other)
         using the area() method. It returns True.....
         if the areas are not equal, and False otherwise.
        '''
        if isinstance(value, Square):
            return self.area() != value.area()
        else:
            return True

    def __gt__(self, value):
        """'>'(greater than sign). The '__gt__' method overloads the..
        .. '>' operator. It compares the areas of two square objects
        ('self' and 'other') using the 'area()' method. it returns 'True'..
        if the area of 'other' and 'False' otherwise.
        """
        if isinstance(value, Square):
            return self.area() > value.area()
        else:
            err_msg = "'>' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __ge__(self, value):
        '''>= (greater than or equal to): The __ge__ method overloads
        the >= operator. It compares the areas of two square objects
        (self and other) using the area() method.
        It returns True if the area of self is greater than or
        equal to the area of other, and False otherwise.
        '''
        if isinstance(value, Square):
            return self.area() >= value.area()
        else:
            err_msg = "'>=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __lt__(self, value):
        '''< (less than): The __lt__ method overloads the < operator.
        It compares the areas of two square objects (self and other) using
        the area() method. It returns True if the area of self is less
        the area of other, and False otherwise.
        '''
        if isinstance(value, Square):
            return self.area() < value.area()
        else:
            err_msg = "'<' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __le__(self, value):
        '''<= (less than or equal to): The __le__ method overloads the
        <=  operator. It compares the areas of two square objects
         (self and other) using the area() method.
         It returns True if the area of self is less than or equal
         to the area of other, and False otherwise.
        '''
        if isinstance(value, Square):
            return self.area() <= value.area()
        else:
            err_msg = "'<=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False
        '''By overloading these comparison operators, the Square class..
        ...allows you to compare two Square objects based on their areas.
        The comparison operators provide a convenient way to determine
        the relative ordering of square objects in terms of their sizes.'''
