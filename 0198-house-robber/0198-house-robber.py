class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        
        def dp(house):
            if house >= len(nums):
                return 0
            if memo[house] == -1:
                memo[house] = max(nums[house] + dp(house+2),dp(house+1))
            return memo[house]
        
        
        
        return dp(0)