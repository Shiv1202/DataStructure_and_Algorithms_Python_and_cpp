# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return
        
        self.swap(root)
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
        
    def swap(self, node):
        if node is None:
            return
        # By Using third variable
#         temp = node.left
#         node.left = node.right
#         node.right = temp
        node.left, node.right = node.right, node.left
