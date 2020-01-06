# Implementation of Merge Sort on linked list.
""" *****************************************
Merge Sort is often preferred for sorting a 
linked list.
NOTE: Basic Algorithm:
merge_sort(head_ref)
1) if the head is NULL or there is only one
    element in the list.
        then return
2) Else divide the list into two halves.
    FrontBackSplit(head, &a, &b):
        where a and b are two halves.
3) Sort the two halves a and b.
    merge_sort(a)
    merge_sort(b)
4) Merge the Sorted a and b(using SortedMerge() 
    given below.)
    and update the head pointer using head_ref.
    *head_ref = SortedMerge(a, b)
*********************************************"""
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked list class.
class Linked_list:
    def __init__(self):
        self.head = None
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    def SortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.SortedMerge(a.next, b)
        else:
            result = b
            result.next = self.SortedMerge(a, b.next)
        return result
    def merge_sort(self, head_ref):
        if head_ref == None or head_ref.next == None:
            return head_ref
        middle = self.get_middle(head_ref)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(head_ref)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.SortedMerge(left, right)
        return sorted_list
    # get_middle Function.
    def get_middle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    # Function for list printing
def print_list(head):
    if head is None:
        print(" ")
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(" ")
if __name__ == '__main__':
    li = Linked_list()
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)

    li.head = li.merge_sort(li.head)
    print("Sorted Linked List is: ")
    print_list(li.head)


    