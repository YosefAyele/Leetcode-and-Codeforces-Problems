class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        a = b = inf
        
        for num in nums:
            if num < a:
                a = num
            elif a < num < b:
                b = num
            elif b < num:
                return True
        
        return False
        
             
        
        
            
            
                