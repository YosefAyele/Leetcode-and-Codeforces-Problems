class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        low = -1
        high = n
        
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            if citations[mid] == n - mid:
                return n - mid
            elif  citations[mid] < n - mid: 
                low = mid
            else:
                high = mid

        return n - high