# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(l)
        return l[k - 1]
