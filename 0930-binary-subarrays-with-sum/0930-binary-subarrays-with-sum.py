class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        sums = {0:1}
        
        runningSum = 0
        res = 0
        
        for i,bit in enumerate(nums):
            
            runningSum += bit
            
            res += sums.get(runningSum - goal,0)
            
            sums[runningSum] = sums.get(runningSum,0) + 1
            
            
        return res
            