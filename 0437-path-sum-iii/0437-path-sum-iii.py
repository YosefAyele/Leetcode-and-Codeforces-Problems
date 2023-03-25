# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans = 0
        
        def calc(node,counts,sum_):
            nonlocal ans
            if not node:
                return
            sum_ += node.val
            
            if sum_ - targetSum in counts:
                ans += counts[sum_ - targetSum]
            
               
            if sum_ in counts:
                counts[sum_] += 1
            else:
                counts[sum_] = 1
            
            calc(node.left,counts,sum_)
            calc(node.right,counts,sum_)
            
            counts[sum_]  -= 1
            if not counts[sum_]:
                del counts[sum_]
            sum_ -= node.val
            
            
        
        calc(root,{0:1},0)
        
        return ans
            