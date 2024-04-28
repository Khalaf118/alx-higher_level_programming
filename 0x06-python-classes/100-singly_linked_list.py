#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Defines a Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialization a new node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data retrieving"""

        return self.__data

    @data.setter
    def data(self, value):
        """data setting"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node retreiving"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setting"""

        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a Singly Linked List"""

    def __init__(self):
        """Initializing a singly linked list"""

        self.__head = []

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)
        """
        new_node = Node(value)
