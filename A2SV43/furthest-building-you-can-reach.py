class Solution:
    def furthestBuilding(self, heights: List[int], b: int, l: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i in range(len(heights)-1):
            curr= heights[i]
            nxt= heights[i+1]
            d=nxt-curr
            
            if d>0:
                heapq.heappush(heap,d)
            
            if len(heap)>l:
                b-=heapq.heappop(heap)
            if b<0:
                return i
            
        return len(heights)-1