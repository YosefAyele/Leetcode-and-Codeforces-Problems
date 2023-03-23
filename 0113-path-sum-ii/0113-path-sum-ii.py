# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(node,curr,sum_):
            nonlocal res
            if not node:
                return 
            sum_ += node.val
            curr.append(node.val)
            
            if not node.left and not node.right:
                if sum_ == targetSum:
                    res.append(curr[:])

            dfs(node.left,curr,sum_)
            dfs(node.right,curr,sum_)
            
            curr.pop()
            # sum_ -= node.val
            
            # return
        dfs(root,[],0)
        
        return res
            
            