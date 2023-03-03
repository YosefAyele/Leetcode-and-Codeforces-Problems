class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def getDay(ship):
            
            curr = 0
            day = 1
            for weight in weights:
                curr += weight
                if curr  > ship:
                    day += 1
                    curr = weight
                
                
            return day
        
        low = weights[0]
        high = 0
        
        for weight in weights:
            low = max(low,weight)
            high += weight
            
        
        low -= 1
        high += 1
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            if getDay(mid) > days:
                low = mid
                
            else:
                high = mid
        
        return high
                
                
        
                    
                    
                