# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        ans = []
        def dfs(node):
            
            if not node:
                return False,None

            val = node.val
            left_valid,left_child = dfs(node.left)
            right_valid,right_child = dfs(node.right)

            if val in to_delete:
                if left_valid:
                    ans.append(node.left)
                if right_valid:
                    ans.append(node.right)
                return False,None

            node.left = left_child
            node.right = right_child

            return True,node
        
        if dfs(root)[0]:
            ans.append(root)
        
        return ans


