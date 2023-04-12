# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            if not node:
                return ""
            
            if not node.left and not node.right:
                return f"{node.val}"
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if right and not left:
                return f"{node.val}()({right})"
            if left and not right:
                return f"{node.val}({left})"
            
            return f"{node.val}({left})({right})"
                
        
        return dfs(root)