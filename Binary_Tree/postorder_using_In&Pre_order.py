# Python Program for Print Postordered traversal using Inorder and Preorder Tarversal.
"""***********************************
A naive method is first construct the tree,
then use simple recursive method to print
postorder traversal of the tree.
NOTE: But We can print postorder traversal 
without coustructing tree.
The idea is, root is always the first ele
of preorder traversal and it must be the 
last ele of postorder traversal.
1) We first recursively print left subtree,
then recursively pritn right subtree, Finally
print root.
**************************************"""
# Function for postorder Traversal.
def print_post_order(inorder, preorder, n):
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])
    if root != 0:
        print_post_order(inorder[:root], preorder[1:root+1], len(inorder[:root]))
    if root != n - 1:
        print_post_order(inorder[root+1:], preorder[root+1:], len(inorder[root+1:]))
    print(preorder[0])

# Main function.
def main():
    inorder = [4, 2, 5, 1, 3, 6]
    preorder = [1, 2, 4, 5, 3, 6]
    n = len(inorder)
    print("Postorder traversal: ")
    print_post_order(inorder, preorder, n)

# Driver Code.
if __name__ == "__main__":
    main()