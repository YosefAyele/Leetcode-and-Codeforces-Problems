# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        
        curr = defaultdict(int)
        temp = head
        idx = 0
        while temp:
            
            while stack and temp.val > stack[-1][0]:
                curr[stack.pop()[1]] = temp.val
            stack.append((temp.val,idx))
            
            idx += 1
            temp = temp.next
        
        return [curr[i] for i in range(idx)]