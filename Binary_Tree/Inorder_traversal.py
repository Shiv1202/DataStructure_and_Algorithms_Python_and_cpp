# Python Program for Inorder Traversal without using recursion.
""" **********************************
Using Stack is the way to traverse Binary 
tree without recursion.
NOTE: Algo for Stack Traversal.
1) Create an empty stack S.
2) Intialize current node as root.
3) Push the current node to S and set
    current = current->left until 
    current is NULL.
4) If current is NULL and stack is not 
    empty then
    a) Pop the top iteam from stack.
    b) Print the popped item, set
        current = popped_item->right.
    c) Go to step 3
5) If Current is NULL and stack is empty
    then we are done.
**************************************"""
# A Binary tree Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative Function for Inorder tree traversal.
def in_order(root):
    current = root
    # Intialize empty stack.
    stack = []
    while True:
        # Reach the leftmost node of the root node.
        if current is not None:
            stack.append(current)
            current = current.left
        # Backtrack from the empty subtree
        # and visit the Node at the top of the 
        # stack.
        elif stack:
            current = stack.pop()
            print(current.data, end = ' ')
            current = current.right
        else:
            break
    print()

# Main Function.
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    in_order(root)

if __name__ == "__main__":
    main()