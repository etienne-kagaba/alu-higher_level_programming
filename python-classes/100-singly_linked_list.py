#!/usr/bin/python3
"""This is a module level docstring"""


class Node:
    """
    A Node
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node
        Args:
            data: integer
            next_node: a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get data
        Returns:
            data
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        Set the data
        Args:
            data: integer

        Returns:
            None
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = data

    @property
    def next_node(self):
        """
        Get next node
        Returns:
            Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        Set the next node
        Args:
            next_node: a Node object

        Returns:
            None
        """
        if not ((isinstance(next_node, Node)) or (next_node is None)):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = next_node


class SinglyLinkedList:
    """
    A singly linked list
    """

    def __init__(self):
        """
        Initializes a singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a value
        Args:
            value: integer

        Returns:
            None
        """
        value = Node(value, None)
        if self.__head is None:
            self.__head = value
        elif self.__head.data > value.data:
            value.next_node = self.__head
            self.__head = value
        else:
            cur = self.__head.next_node
            temp = self.__head
            while cur is not None:
                if cur.data >= value.data:
                    break
                cur = cur.next_node
                temp = temp.next_node
            value.next_node = cur
            temp.next_node = value

    def __str__(self):
        """
        Returns a string representation of the singly linked list
        Returns:
            string
        """
        out = ''
        if self.__head is None:
            out = ''
        else:
            temp = self.__head
            while temp is not None:
                out += f'{temp.data}\n'
                temp = temp.next_node

        return out.strip('\n')
