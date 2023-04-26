# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(node,parent,gparent):
            nonlocal res 
            if not node:
                return
            
            if gparent % 2 == 0:
                res += node.val
            dfs(node.left,node.val,parent)
            dfs(node.right,node.val,parent)
        
        dfs(root,-1,-1)
        
        return res
                
            