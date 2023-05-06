class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        
        heapq.heapify(heap)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heapq.heappush(heap,-matrix[row][col])
                
                if len(heap) > k:
                    heapq.heappop(heap)
                  
        return -heapq.heappop(heap)