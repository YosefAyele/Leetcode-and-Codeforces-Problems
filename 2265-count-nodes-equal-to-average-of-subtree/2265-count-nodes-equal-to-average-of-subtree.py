# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        
        def checkAvg(node):
            nonlocal res
            if not node:
                return (0,0)
            
            leftCount , leftSum = 0, 0 
            rightCount, rightSum = 0, 0 
            
            left = checkAvg(node.left)
            right = checkAvg(node.right)
            
            leftCount += left[1]
            leftSum += left[0]
            
            rightCount += right[1]
            rightSum += right[0]
            
            currSum = leftSum + rightSum + node.val
            currCount = leftCount + rightCount + 1
            
           
            if currSum // currCount ==  node.val:
                res += 1
            return (currSum,currCount)
        
        checkAvg(root)
        
        return res
        
                

            