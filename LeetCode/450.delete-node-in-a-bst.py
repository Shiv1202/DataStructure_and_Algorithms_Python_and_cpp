#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderSuccessor(self, node: TreeNode):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            t = self.inorderSuccessor(root.right)
            root.val = t.val
            root.right = self.deleteNode(root.right, t.val)
        return root
        
# @lc code=end

