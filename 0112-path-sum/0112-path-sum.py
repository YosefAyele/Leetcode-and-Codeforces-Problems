# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(node,sum_):
            
            if not node:
                return 
            
            sum_ += node.val
            if not node.left and not node.right:
                if sum_ == targetSum:
                    return True

            
            left = dfs(node.left,sum_)
            right = dfs(node.right,sum_)
            
            sum_ -= node.val
            
            return left or right
            
        
        return dfs(root,0)