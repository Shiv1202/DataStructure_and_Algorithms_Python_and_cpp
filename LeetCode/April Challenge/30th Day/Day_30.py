# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr)
        
        def visited(node, index):
            if index == n - 1:
                if node is not None and node.val == arr[index]:
                    return node.left is None and node.right is None
                return False
            if node is None:
                return False
            if node.val == arr[index]:
                return visited(node.left, index + 1) or visited(node.right, index + 1)
            return False
        
        return visited(root, 0)
