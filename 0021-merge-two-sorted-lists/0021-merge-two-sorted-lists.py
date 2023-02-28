# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def merge(head1,head2,dummy):
            
            if not head1:
                dummy.next = head2
                return dummy
            elif not head2:
                dummy.next = head1
                return dummy
            
            if head1.val < head2.val:
                dummy.next = head1
                dummy = dummy.next
                return merge(head1.next,head2,dummy)
            else:
                dummy.next = head2
                dummy = dummy.next
                return merge(head1,head2.next,dummy)
            
            
        
        dummyNode = ListNode(0)
        dummy = dummyNode
        
        res = merge(list1,list2,dummy)
        
        return dummyNode.next