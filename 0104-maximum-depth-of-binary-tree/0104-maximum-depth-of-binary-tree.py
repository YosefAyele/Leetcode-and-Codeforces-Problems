# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
      
        
        def findDepth(node):
            
            if not node:
                return 0
            
      
            l= r = 0
            l += findDepth(node.left)
            r += findDepth(node.right)
            return max(l,r) + 1
        
        return findDepth(root)
            
        