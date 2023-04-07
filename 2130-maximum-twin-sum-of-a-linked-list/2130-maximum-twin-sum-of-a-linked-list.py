# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        maxtsm=0
        while fast:
            fast=fast.next.next
            slow=slow.next  
        revsl=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=revsl
            revsl=curr
            curr=nxt 
        temp=head
        while revsl:
            sm=revsl.val+temp.val
            if sm>maxtsm:
                maxtsm=sm
            revsl=revsl.next
            temp=temp.next

              
        return maxtsm
            
            
        