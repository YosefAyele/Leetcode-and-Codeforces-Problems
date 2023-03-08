# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(node1,node2):
            
            if not node1:
                return not node2
            if not node2:
                return not node1
            
            if node1.val != node2.val:
                return False
            
            left = check(node1.left,node2.left)
            right = check(node1.right,node2.right)
            
            return left and right
        
        return check(p,q)