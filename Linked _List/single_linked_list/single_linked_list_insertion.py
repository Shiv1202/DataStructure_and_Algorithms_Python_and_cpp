# Implementation of Single Linked List.
"""*************************************
NOTE: (Linked List Creation and Traversal.)
1) linked list is represented by a pointer
to the first node of the list.
2) Each node in a list consist at least
two parts:
    a) Data part.
    b) Pointer (or reference) to the next node.
****************************************"""
# Node Class 
class Node:
    """ Function to initiakize the node
    object."""
    def __init__(self, data):
        self.data = data    # Assign data
        self.next = None    # next node add.

# Linked List class.
class Linkedlist:
    """ Function to initialize the linked
    list object."""
    def __init__(self):
        self.head = None
        """ Function for printing the 
        contents of linked list."""
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next