# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findCommon(node):
            
            if not node:
                return 
            
            if p.val <= node.val <= q.val:
                return node
            elif p.val < node.val and q.val < node.val:
                return findCommon(node.left)
            elif p.val > node.val and q.val > node.val:
                return findCommon(node.right)
            
            return node
        
        return findCommon(root)