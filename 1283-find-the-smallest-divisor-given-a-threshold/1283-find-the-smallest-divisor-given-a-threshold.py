class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def summ(divisor):
            
            res = 0
            
            for num in nums:
                
                res += ceil(num/divisor)
                
            return res
        
        low = 0
        high = sum(nums) + 1
        
        while high > low + 1:
            
            mid = low + (high - low)//2
            
            if summ(mid) > threshold:
                low = mid
            else:
                high = mid
        
        return high