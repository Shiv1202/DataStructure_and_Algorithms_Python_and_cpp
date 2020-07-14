# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        temp = head
        while temp != None:
            n += 1
            temp = temp.next
        for i in range(n // 2):
            head = head.next
        return head
