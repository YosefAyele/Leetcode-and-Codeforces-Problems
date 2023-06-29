class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(target):
            
            if target == 0:
                return 1
            elif target < 0:
                return 0
            
            cur = 0
            for num in nums:
                if target >= num:
                    cur += dp(target-num)
                    
            return cur
        
        return dp(target)