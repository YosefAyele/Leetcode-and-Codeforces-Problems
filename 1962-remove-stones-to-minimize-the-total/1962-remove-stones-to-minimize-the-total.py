class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        
        
        for _ in range(k):
            val = heapq.heappop(heap)
            heapq.heappush(heap, val//2)
            
        return -sum(heap)
            
                    
            