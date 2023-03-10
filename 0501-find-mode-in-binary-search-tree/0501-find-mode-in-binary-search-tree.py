# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        counts = {}
        def mode(node):
            nonlocal counts
            if not node:
                return 
            
            mode(node.left)
            
            counts[node.val] = counts.get(node.val,0) + 1
            
            mode(node.right)
        
        mode(root)
        
        maxCount = max(counts[i] for i in counts)
        
        res = []
        
        for num in counts:
            if counts[num] == maxCount:
                res.append(num)
                
        
        return res
                
        
        