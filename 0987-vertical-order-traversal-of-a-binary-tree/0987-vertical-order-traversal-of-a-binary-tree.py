# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def findHeight(node):
            
            if not node:
                return 0
            left = right = 0
            
            left += findHeight(node.left)
            right += findHeight(node.right)
            
            return max(left,right) + 1
        
        maxHeight = findHeight(root) 
        
        maxWidth = 2**(maxHeight-1) + 1
        
        res = [[] for i in range(maxWidth)]
        
        def addElement(node,index,level,precedence):
            
            if not node:
                return 
            
            if level == 0:
                res[index].append((precedence,node.val))
                
            addElement(node.left,index - 1, level - 1,precedence+1)
            addElement(node.right,index + 1, level - 1,precedence+1)
            
            return
        for i in range(maxHeight):
            
            addElement(root,maxWidth//2,i,0)
        
        ans = []
        
        for vertical in res:
            if vertical:
                vertical.sort()
                curr = []
                for node in vertical:
                    curr.append(node[1])
                ans.append(curr)
        
        return ans