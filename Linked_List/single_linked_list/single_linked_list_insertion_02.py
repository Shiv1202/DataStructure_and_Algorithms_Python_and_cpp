# Implementation of Single Linked List.
"""*************************************
NOTE: (Linked List Insertion.) Part-2
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
        a node after given node."""
    def insert_after(self, prev_node, new_data):
        # Check if the given node is exists.
        if prev_node is None:
            print("The given Previous node not in list.")
            return
        # Create new node and put data.
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
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
    L_list.insert_after(2, 4)
    # Print List
    L_list.print_list()