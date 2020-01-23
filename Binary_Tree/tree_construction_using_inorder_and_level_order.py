# Python Program for tree Construction Using Inorder and level order seq.
# Class for binary node.
class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

def build_tree(level, inorder):
    if inorder:
        for i in range(len(level)):
            if level[i] in inorder:
                node = Node(level[i])
                io_index = inorder.index(level[i])
                break
        if not inorder:
            return node
        node.l = build_tree(level, inorder[0:io_index])
        node.r = build_tree(level, inorder[io_index + 1:len(inorder)])
        return node
def print_inorder(node):
    if node is None:
        return
    print_inorder(node.l)
    print(node.data, end = " ")
    print_inorder(node.r)

# Main Function.
def main():
    level_order = [20, 8, 22, 4, 12, 10, 14]
    inoder = [4, 8, 10, 12, 14, 20, 22]
    root = build_tree(level_order, inoder)
    print("Inorder Traversal of the constructed Binary tree.")
    print_inorder(root)

if __name__ == "__main__":
    main()
