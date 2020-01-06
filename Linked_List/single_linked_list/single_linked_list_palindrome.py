"""Python program for check if a singly linked
list is Palindrome."""
""" *****************************************
Problem:
Given a singly linked list of characters/Numbers.
Return True if the given list is a Palindrome,
else False.
NOTE: Method 1 (Use a Stack)
1) A simple solution is to use a stack of list 
nodes. This mainly involves three steps.
    a) Traverse the given list from head to
    tail and push every visited node to stack.
    b) Traverse the list again. For every visited
    node, pop a node from stack and compare data 
    of popped node with currently visited node.
    c) If all nodes matched, then return True
    Else False.
*********************************************"""
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

# Function for Palindrome.
def is_palindrome(L_list):
    start = L_list.head
    stack = []
    #count = 0
    while start:
        stack.append(start.data)
        start = start.next
    while start:
        if start.data != stack.pop():
            return False
        start = start.next
    return True

# Driver Code.
if __name__ == "__main__":
    # Start with empty linked list.
    L_list = Linkedlist()
    L_list.head = Node(1)
    second = Node(2)
    third = Node(1)
    # Now Link first node with second
    L_list.head.next = second
    # And second node with third
    second.next = third
    result = is_palindrome(L_list)
    print(result)