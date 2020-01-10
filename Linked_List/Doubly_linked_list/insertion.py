# Python Program for Doubly Linked list.
"""*************************************
A Doubly Linked List(DLL) contains an extra
pointer, typically called previous pointer.
NOTE: Insertion Methods.
1) Add a node at the front.
    (A 5 step process)
2) Add a node after a given node.
    (A 7 step process)
3) Add a node at the end of list.
    (A 7 step process)
****************************************"""
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
    # Function for insert node at Front.
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Function for insert new node after given node.
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Node doesn't Exists in DLL.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    # Function for insert new node at end of list.
    def append(self, new_data):
        new_node = Node(new_data)
        last = self.head
        new_node.next = None
        """ If the Linked List is empty 
            Make the new_node as head."""
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Function for print the list.
    def print_list(self):
        temp = self.head
        if self.head is not None:
            while temp:
                print(temp.data, end = " ")
                temp = temp.next
                if temp == self.head:
                    break
# Main Function.
def main():
    D_list = D_linked_list()
    D_list.push(2)
    D_list.push(56)
    D_list.push(75)
    D_list.push(7)
    D_list.append(101)
    D_list.insert_after(D_list.head.next, 145)
    # Print the list
    D_list.print_list()

if __name__ == "__main__":
    main()