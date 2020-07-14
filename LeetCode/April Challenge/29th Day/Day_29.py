# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.total = float('-inf')
        
        def recur(node):
            if not node:
                return 0
            left_sum = recur(node.left)
            right_sum = recur(node.right)
            
            till_max = max(node.val, node.val + max(left_sum, right_sum))
            
            self.total = max(self.total, till_max, node.val + left_sum + right_sum)
            return till_max
        
        return max(recur(root), self.total)
