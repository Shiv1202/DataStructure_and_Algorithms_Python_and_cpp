# Python Program for Inorder Traversal without recursion and stack.
# (Morris inorder traversal)
"""************************************
The idea of Morris Traversal is based on 
Threaded Binary Tree. In this traversal,
we first create links to inorder successor 
and print the data using these links.
***************************************"""
# Binary Tree Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None
# Morris Method.
def morris_traversal(root):
    curr = root
    while curr is not None:
        if curr.l is None:
            print(curr.data)
            curr = curr.r
        else:
            pre = curr.l
            while pre.r is not None and pre.r != curr:
                pre = pre.r
            if pre.r is None:
                pre.r = curr
                curr = curr.l
            else:
                pre.r = None
                print(curr.data)
                curr = curr.r

# Main Function.
def main():
    root = Node(1)
    root.l = Node(2)
    root.r = Node(3)
    root.l.l = Node(4)
    root.l.r = Node(5)
    morris_traversal(root)
# Driver Code.
if __name__ == "__main__":
    main()