# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        vertical = {}
        
        def dfs(node,row,col):
            
            if not node:
                return
            
            if col in vertical:
                vertical[col].append((row,node.val))
            else:
                vertical[col] = [(row,node.val)]
            
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
            
            return
        dfs(root,0,0)
        ans = []
        
        for i in sorted(vertical):
            curr = vertical[i]
            
            curr.sort()
            newCurr = [curr[i][1] for i in range(len(curr)) ]
            
            ans.append(newCurr)
        
        return ans
        