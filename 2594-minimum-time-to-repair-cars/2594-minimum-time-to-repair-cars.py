class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def ok(time):
            res = 0
            
            for rank in ranks:
                res += int((time//rank)**0.5)
                
            return res
        
        low = 0
        high = max(ranks) * (cars**2)
        
        while high > low + 1:
            mid = low + (high - low)//2
            
            if ok(mid) >= cars:
                high = mid
            else:
                low = mid
        
        return high