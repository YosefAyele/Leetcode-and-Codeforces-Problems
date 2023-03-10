# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def helper(node):
            # base case
            
            if not node or not node.next:
                return node
            
            # step 1 is dividing the current linked list into two halves
            
            slow = None
            fast = node
            while fast and fast.next:
                slow = node if not slow else slow.next
                fast = fast.next.next
                
            
            temp = slow.next
            slow.next = None
            
            left = node
            right = temp
            
            head1 = helper(left)
            head2 = helper(right)
            
            # now merge
            
            merged = ListNode(0)
            temp = merged
            
            while head1 and head2:
                
                if head1.val < head2.val:
                    temp.next = head1
                    head1 = head1.next
                    
                else:
                    temp.next = head2
                    head2 = head2.next
                
                temp = temp.next
            temp.next= head1 if head1 else head2
            return merged.next
        
        return helper(head)
                    