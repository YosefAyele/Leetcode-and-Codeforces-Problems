# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         temp=head
#         while temp:
#             curr=head
#             while curr!=temp:
#                 if curr.val>temp.val:
#                     curr.val,temp.val=temp.val,curr.val
#                 curr=curr.next
    
#             temp=temp.next
#         return head
            
        sortd=ListNode(0,head)
        
        prev, curr = head, head.next
        
        while curr:
            if curr.val>=prev.val:
                prev,curr=curr, curr.next
                continue
            
            temp=sortd
            
            while curr.val>temp.next.val:
                temp=temp.next
            prev.next=curr.next
            curr.next=temp.next
            temp.next=curr
            curr=prev.next
        return sortd.next