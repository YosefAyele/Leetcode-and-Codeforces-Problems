class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def totalHours(speed):
            res = 0
            for pile in piles:
                
                res += ceil(pile/speed)
            
            return res
        
        
        low = 0
        high = max(piles) + 1
        
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            currTotal = totalHours(mid)
            # print(speed," ",currTotal)
            
            if currTotal > h:
                low = mid
                
            else:
                # print(high)
                high = mid
                
        return high
                
        
        
            