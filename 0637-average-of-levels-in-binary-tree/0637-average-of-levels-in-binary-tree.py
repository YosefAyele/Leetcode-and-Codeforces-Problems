# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque()
        
        queue.append(root)
        
        res = []
        while queue:
            
            length = len(queue)
            currSum = 0
            for i in range(length):
                curr = queue.popleft()
                if curr:
                    currSum += curr.val
                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
            res.append(currSum/length)
        
        return res
                
                
                
