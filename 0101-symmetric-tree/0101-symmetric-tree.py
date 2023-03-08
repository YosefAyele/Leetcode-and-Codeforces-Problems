# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(node1,node2):
            
            if not node1:
                return not node2
            if not node2:
                return not node1
            if node1.val != node2.val:
                return False
            left1 = node1.left
            left2 = node2.left
            right1 = node1.right
            right2 = node2.right
            
            # outers are left1 and right2
            if not left1 and not right2:
                checkOuters = True
            elif not left1 and  right2:
                checkOuters = False
            elif left1 and not right2:
                checkOuters = False
            else:
                checkOuters = left1.val == right2.val
            # inners are right1 and left2
            
            if not right1 and not left2:
                checkInners = True
            elif not right1 and left2:
                checkInners = False
            elif right1 and not left2:
                checkInners = False
            else:
                checkInners = right1.val == left2.val
            
            if not (checkInners and checkOuters):
                return False
            outers = symmetric(left1,right2)
            inners = symmetric(right1,left2)
            
            return outers and inners
        if not root.left and not root.right:
            return True
        elif not root.left and root.right:
            return False
        elif root.left and not root.right:
            return False
        else:
            return symmetric(root.left,root.right)
            
            