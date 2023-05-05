# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = ListNode(0)
        tail = res
        heap = []
        
        for lst in lists:
            temp = lst
            while temp:
                heap.append(temp.val)
                temp = temp.next
                
        heapq.heapify(heap)
        
        while heap:
            
            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next
        
        return res.next
            
        