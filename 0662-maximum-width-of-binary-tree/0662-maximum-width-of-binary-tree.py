# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        rowCol = {}
        
        def dfs(node,row,col):
            nonlocal rowCol
            
            if not node:
                return
            
            if row in rowCol:
                min_ , max_ = rowCol[row]
                min_ = min(min_,col)
                max_ = max(max_,col)
                
                rowCol[row] = (min_,max_)
            else:
                rowCol[row] = (col,col)
            dfs(node.left,row + 1, col*2)
            dfs(node.right,row+1,col*2 + 1)
            
        dfs(root,0,0)
        
        res = 0
        for row in rowCol:
            level = rowCol[row]
            res = max(res,level[1]-level[0])
        
        return res + 1
        