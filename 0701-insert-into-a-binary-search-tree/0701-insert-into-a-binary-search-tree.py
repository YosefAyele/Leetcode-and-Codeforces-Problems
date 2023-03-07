# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insertNode(node,val):
            
            if not node:
                newNode = TreeNode(val)
                return newNode
            
            if node.val > val:
                node.left = insertNode(node.left,val)
                    
            else:
                node.right = insertNode(node.right,val)
            
            return node
        
        
        
        return insertNode(root,val)
                
                 
            
        
        
