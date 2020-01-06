# Python Program to split circular linked list into two halves.
""" **********************************
If there are Odd number of nodes, then
first list should contain one extra.
1) Store the mid and last pointers of the
circular linked list.
2) Make the second half circular.
3) Make the first half circular.
4) Set head (or start) pointer of both
linked list.
**************************************"""
# Node class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class.
class C_linked_list:
    def __init__(self):
        self.head = None

    # Function for insert node at start.
    def push(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    # Function for print list.
    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end = " ")
                temp = temp.next
                if temp == self.head:
                    break

    def split_list(self, head_1, head_2):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is None:
            return
        """ If there is Odd nodes in the circular list
        then fast_ptr -> next become head and
        for Even nodes
        fast_ptr -> next -> next becomes head."""
        while fast_ptr.next != self.head and fast_ptr.next.next != self.head:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        """ If there are even element in list
            then move fast_ptr"""
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next
        # Set the pointer head of the first half.
        head_1.head = self.head
        # Set the pointer head of the Second half.
        if self.head.next != self.head:
            head_2.head = slow_ptr.next
        # Make second half circular.
        fast_ptr.next = slow_ptr.next
        # Make first half circular.
        slow_ptr.next = self.head
# Main Function.
def main():
    c_list = C_linked_list()
    head_1 = C_linked_list()
    head_2 = C_linked_list()
    c_list.push(56)
    c_list.push(12)
    c_list.push(11)
    c_list.push(112)
    c_list.push(2)
    print("Original Circular Linked List:")
    c_list.print_list()
    # Split the list.
    c_list.split_list(head_1, head_2)
    print("\nFirst Circular Linked List:")
    head_1.print_list()
    print("\nSecond Circular Linked List:")
    head_2.print_list()

if __name__ == "__main__":
    main()