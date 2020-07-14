# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        
        stack = []
        stack.append(root)
        i = 1
        while i < len(preorder):
            temp = None
            while len(stack) > 0 and preorder[i] > stack[-1].val:
                temp = stack.pop()
            
            if temp != None:
                temp.right = TreeNode(preorder[i])
                stack.append(temp.right)
            
            else:
                temp = stack[-1]
                temp.left = TreeNode(preorder[i])
                stack.append(temp.left)
            i = i + 1
        return root
