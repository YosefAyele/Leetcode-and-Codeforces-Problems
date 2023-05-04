class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = heappop(heap)
            x = heappop(heap)
            heapq.heappush(heap,y-x)
            
        return -heappop(heap)
            
            
        