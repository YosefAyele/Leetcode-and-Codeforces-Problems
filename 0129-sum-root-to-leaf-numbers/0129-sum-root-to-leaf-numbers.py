# Definiti\7/7]\n for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(node,curr):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                ans = ''.join(curr) + str(node.val)
                res += int(ans)
                return
                
            curr.append(str(node.val))
            
            dfs(node.left,curr.copy())
            dfs(node.right,curr.copy())
        
        dfs(root,[])
        
        return res