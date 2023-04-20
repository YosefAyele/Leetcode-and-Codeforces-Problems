# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        tail.next = head
        
        prev_val = None
        
        while head and head.next:
            
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                tail.next = head.next
            else:
                tail = tail.next
            
            head = head.next
            
       
                    
              
        
        return dummy.next

        
        