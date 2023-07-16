#!/usr/bin/python3

"""
File_name: 100-singly_linked_list.py
Created: 30th of May, 2023
Auth: Daniel Nyong (Danyhoney)
Size: undefined
Project: 0x06-python-classes
Status: submitted.
"""


class Node:

    """
    # This Code consist of Two Classes 'Node' and 'SinglyLinkedList...
    # Write a class Node that defines a node of a singly linked list by:
    # Private instance attribute: data:
    # property def size(self): to retrieve it....
    # property setter def size(self, value): to set it:
    # VARIABLE(" "):
    # class(Node): Singly linked list
    # Return: Always 0. (Success)
    """
    """The Node class represents a node of a singly linked list...
    ...it has private instance attributes 'data' and 'next_node'"""
    """which can be accessed using getter and setter methods"""
    """a default value of 0. it will perform the below checks..."""
    def __init__(self, data, next_node=None):
        """ Th 'Node' class has two private instance attributes...
        ...'data' and 'next_node'..."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ decorator is used to define a getter method"""
        return self.__data

    @data.setter
    def data(self, value):
        """ decorator is used to define a setter method"""
        """ If the 'data' is not an instance of 'int', it raises a 'TypeError
        ...Exception with the message 'Data Must Be An Integer' """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ decorator is used to define a getter method"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ decorator is used to define a setter method"""
        """ If the 'size' is not an instance of 'int', it raises a 'TypeError
        ...Exception with the message 'Size Must Be An Integer' """
        if value is None and isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    # Ths class represents a singly linked list. it has a private...
    # ....instance attribute 'head', which is the starting point of the....
    # ...list. The class provide a 'sorted_insert' method to insert a new...
    # ...'Node' into the correct sorted position in increasing order.."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """The singly linked list has one private instance attribute 'head..
        which points to the first node in the list...
        ..The class also has a 'sorted_insert' method, which takes a ....
        value as input and inserts a new node into the correct sorted....
        position in the list in increasing order...."""
        new_node = Node(value)
        if not isinstance(value, int) or value is None:
            raise TypeError("value must be an integer")
        else:
            if self.__head is None or self.__head.data >= value:
                new_node = Node(value, self.__head)
                self.__head = new_node
            else:
                nodes = self.__head
                op_nodes = None
                while nodes is not None and value > op_nodes.data:
                    op_nodes = nodes
                    nodes = nodes.next_node
                new_node = Node(value, nodes)
                op_nodes.next_node = new_node

    def __str__(self):
        nodes = self.__head
        """'__str__' method is defined to allow printing the entire list by..
        iterating over the nodes and returning a string representation of...
        data values..."""
        op_nodes = []
        while nodes is not None:
            op_nodes.append(str(nodes.data))
            nodes = nodes.next_node
        return '' if len(op_nodes) == 0 else '\n'.join(op_nodes)
