""" Implementation of Circular Linked List
in python3."""
""" *************************************
Insertion at start and Traversal of Circular 
Linked List.
*****************************************"""
# Node class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked List class.
class Linked_list:
    def __init__(self):
        self.head = None

    """ Function for insert a node at the beginning of a
     Circular list."""
    def push(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head
        # if list is not None then set the next of last Node.
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            #for the first node
            new_node.next = new_node 
        self.head = new_node
    # Function for printing of list.
    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end = " ")
                temp = temp.next
                if temp == self.head:
                    break
def main():
    c_list = Linked_list()
    # Create Linked list will be 17 -> 45 -> 2 -> 56.
    c_list.push(56)
    c_list.push(2)
    c_list.push(45)
    c_list.push(17)
    # Print List.
    c_list.print_list()
    