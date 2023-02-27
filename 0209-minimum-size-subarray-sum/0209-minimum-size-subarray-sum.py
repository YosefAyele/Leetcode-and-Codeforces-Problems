class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        minLength = len(nums) + 1
        runningSum = 0
        left = 0
        for right,num in enumerate(nums):
            
            runningSum += num
            
            while runningSum >= target:
                minLength = min(right - left + 1, minLength)
                runningSum -= nums[left]
                left += 1
            
            
        
        return minLength if minLength < len(nums) + 1 else 0
            
            