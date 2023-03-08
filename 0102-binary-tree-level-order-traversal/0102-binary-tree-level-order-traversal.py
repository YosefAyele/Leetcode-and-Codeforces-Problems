# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def findHeight(node):
            
            if not node:
                return 0
            left = right = 0
            
            left += findHeight(node.left)
            right += findHeight(node.right)
            
            return max(left,right) + 1
        
        def getLevel(node,level,res):
            
            if not node:
                return res
            if level == 0:
                res.append(node.val)
            
            getLevel(node.left,level - 1,res)
            getLevel(node.right,level - 1,res)
            
            return res
            
        height = findHeight(root)
        
        ans = []
        for i in range(height):
            
            curr = getLevel(root,i,[])
            ans.append(curr)
        
        return ans