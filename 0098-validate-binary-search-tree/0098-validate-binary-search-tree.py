# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node,left,right):
            if not node:
                return True

            
            
            if not (left < node.val < right):
                return False
            leftCheck = valid(node.left,left,node.val)
            rightCheck = valid(node.right,node.val,right)
            
            return leftCheck and rightCheck
    
            
        
        return valid(root,-inf,inf)