# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def track(node,currList):
            nonlocal res
            if not node:
                return
            
            currList.append(str(node.val))
            
            if not node.left and not node.right:
                string = "->".join(currList)
                res.append(string)
                return
            
            
            track(node.left,[num for num in currList])
            
            track(node.right,[num for num in currList])
            
            
            return 
        
        track(root,[])
        
        return res
    