# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        
        q.append(root)
        
        res = []
        while q:
            
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr and  curr.left:
                    q.append(curr.left)
                if curr and  curr.right:
                    q.append(curr.right)
                    
                if curr:
                    level.append(curr.val)
            if level:  
                res.append(level)
                
        return res[::-1]