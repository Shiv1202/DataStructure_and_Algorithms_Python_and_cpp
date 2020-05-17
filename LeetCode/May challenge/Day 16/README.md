# Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the `node number` and `not the value` in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

**Note**
* The relative order inside both the even and odd groups should remain as it was in the input.
* The first node is considered odd, the second node even and so on ...

**Example 1**

```
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

**Example 2**

```
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```

## Solution
Put the odd nodes in a linked list and the even nodes in another. Then link the evenList to the tail of the oddList.

A well-formed LinkedList need two pointers head and tail to support operations at both ends. The variables `head` and `odd` are the head pointer and tail pointer of one LinkedList we call `oddList`, the variables `temp` and `even` are the head pointer and tail pointer of another LinkedList we call `evenList`. The algorithm traverses the original LinkedList and put the odd nodes into the oddList and the even nodes into the evenList. To traverse a LinkedList we need at least one pointer as an iterator for the current node. But here the pointers odd and even not only serve as the tail pointers but also act as the iterators of the original list.

**Approach**
* we have a `head` pointer pointing to the `digit 1 or the 1st index`.
* we declare 2 pointers `odd` pointer to `iterate over the odd indices` and an `even` pointer to `iterate over the even indices`.
 the `odd` is assigned the `1st index` and the `even` is assigned the `2nd index`.
 ```
 ListNode* odd=head;
 ListNode* even=head->next;
 ```
* as we have to concatinate `even indices` after the `odd indices` we declare a `temporary pointer or temp` to `preserve the start of the even indices linkedlist`.
```
ListNode* temp=head->next;
```
* now, with this `odd` pointer we assign it values such that it connects to the next `odd index` and so on...
 Similarly for the `even` pointer we follow the same process.
 ```
 while(odd->next && even->next)
        {
            odd->next=odd->next->next;
            odd=odd->next;
            
            even->next=even->next->next;
            even=even->next;
        }
        //here 1 connects to 3 , 3 connects to 5 , and so on
        //1->3->5->7...
        //similarly, 2->4->6->8...
 ```
 * at last, we assign the the preserved start of even indices, `temp` to the `next of odd pointer`, and return the `head`
 ```
        odd->next=temp;
        return head;
 ```

