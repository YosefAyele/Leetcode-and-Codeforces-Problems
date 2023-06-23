class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        
        memo = [defaultdict(lambda:-inf) for i in range(len(nums))]
        
        def dp(summ,idx):
            if idx >= len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
            if  memo[idx][summ] == -inf:
                add = dp(summ + nums[idx],idx +1)
                subtract = dp(summ - nums[idx],idx + 1)
                
                memo[idx][summ] = add + subtract
            return memo[idx][summ]
        
        return dp(0,0)