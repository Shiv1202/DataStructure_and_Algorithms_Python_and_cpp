# Python Program to Delete a node in DLL.
""" ************************************
Time Complexity = O(1)
NOTE: Algorithm-> Let the node to be deleted is del.
1) If node to be deleted is head node, then change the head pointer to nextcurrent head.
2) Set next of previous to del exists.
3) Set prev of next to del, if next to del exists.
****************************************"""
import gc   # For Garbage collection
# Node class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Linked List class.
class D_linked_list:
    def __init__(self):
        self.head = None
    # Function for delete a node.
    def delete_node(self, del_node):
        # Base Case
        if self.head is None or del_node is None:
            return
        # If deleted node is head.
        if self.head == del_node:
            self.head = del_node.next
        # Change prev only if node to be deleted is NOT
        # the last node.
        if del_node.next is not None:
            del_node.next.prev = del_node.prev
        if del_node is not None:
            del_node.prev.next = del_node.next
        # Finally Free the memory
        gc.collect()
    
    # Function for insert node at Front.
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Function for print the list.
    def print_list(self, node):
        while node is not None:
            print(node.data, end = " ")
            node = node.next
# Driver code.
dll = D_linked_list()
dll.push(10)
dll.push(8)
dll.push(4)
dll.push(2)
print("Original Linked List:\n")
dll.delete_node(dll.head)
dll.delete_node(dll.head.next)
dll.delete_node(dll.head.next)
print("Modified Linked List:\n")
dll.print_list(dll.head)

