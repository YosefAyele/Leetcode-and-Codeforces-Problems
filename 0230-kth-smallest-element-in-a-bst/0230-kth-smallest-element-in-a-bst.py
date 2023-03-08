# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        counter = 0
        ans = root.val
        
        def findKth(node):
            nonlocal counter,ans
            if not node:
                return 
            
            findKth(node.left)
            counter += 1
            if counter == k:
                ans = node.val
            findKth(node.right)
            
            return ans
            
        return findKth(root)