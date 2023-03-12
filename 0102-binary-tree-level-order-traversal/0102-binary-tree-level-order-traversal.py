# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            iterations = len(queue)
            
            for _ in range(iterations):
                currLevel = queue.popleft()
                if currLevel:
                    if currLevel.left:
                        queue.append(currLevel.left)
                    if currLevel.right:
                        queue.append(currLevel.right)

                    level.append(currLevel.val)
            if level:   
                res.append(level)
        
        return res
            
            
            
        