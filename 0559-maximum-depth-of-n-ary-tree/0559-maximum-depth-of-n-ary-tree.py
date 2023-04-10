"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        
        if not root:
            return 0
        def dfs(node,parent,depth):
            nonlocal ans
            ans = max(ans,depth + 1)
            for child in node.children:
                if child != parent:
                    cur_depth = dfs(child,node,depth + 1)
                    
            
            return
        dfs(root,-1,0)
        
        return ans