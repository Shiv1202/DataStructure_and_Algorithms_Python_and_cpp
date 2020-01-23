# Python Program to find Max Depth or Height of a tree.
"""************************************
NOTE: Algo
max_depth()
1) if tree is empty then return 0
2) else
    a) Get the max depth of left-subtree.
    b) Get the max depth of right-subtree.
    c) Get the max depth of left and right
    subtree and add 1 to it for the current 
    node.
    d) Return max_depth
***************************************"""
# Binary tree class.
class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None
# Function for max Depth.
def max_depth(node):
    if node is None:
        return 0
    else:
        l_depth = max_depth(node.l)
        r_depth = max_depth(node.r)
        # Use the larger one.
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

# Main Function
def main():
    root = Node(1)
    root.l = Node(2)
    root.r = Node(3)
    root.l.l = Node(4)
    root.l.r = Node(5)
    print("Max Depth of Tree is: " + str(max_depth(root)))

# Driver Code.
if __name__ == "__main__":
    main()