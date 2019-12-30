# Implementation of Single Linked List.
"""*************************************
NOTE: (Linked List Insertion.)
Inserting a node in a list done by 3 ways.
1) At the front of the linked list.
2) After a given node.
3) At the end of the linked list.
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
        """ Function for inserting 
        a node at the start of List."""
    def push_start(self, new_data):
        # Allocating new node with new_data.
        new_node = Node(new_data)
        # Make next of new Node as head.
        new_node.next = self.head
        # Move head to point to new node.
        self.head = new_node
        """ Function for printing the 
        contents of linked list."""
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

# Driver Code.
if __name__ == "__main__":
    # Start with empty linked list.
    L_list = Linkedlist()
    L_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    # Now Link first node with second
    L_list.head.next = second
    # And second node with third
    second.next = third
    # Inserting New Node.
    L_list.push_start(4)
    # Print List
    L_list.print_list()