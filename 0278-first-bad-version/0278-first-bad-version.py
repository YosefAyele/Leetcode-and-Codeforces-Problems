# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        low = -1
        high = n
        # ans = -1
        
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            if not isBadVersion(mid):
                low = mid 
            
            else:

                high = mid 
            
            
        
        return high
            
            
        