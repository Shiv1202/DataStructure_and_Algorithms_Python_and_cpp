# Python Program for Reverse a DLL.
""" ********************************
NOTE: Simple Mehode for reversing a Doubly 
Linked List, All we need to do is swap prev
and next pointer of all nodes, change prev
of the head(or start) and change the head
pointer in end.
************************************"""
# Node class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Linked List class.
class D_linked_list:
    def __init__(self):
        self.head =None
        