class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        
        high = x 
        mid = low + (high - low)//2
        while low <= high:
            
            curr = mid**2
            
            if curr == x:
                return mid
            
            elif curr > x:
                high = mid - 1
            
            else:
                low = mid + 1

            mid = low + (high - low)//2
        return mid