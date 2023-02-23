class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        running_sum = 0
        max_sum = nums[0]
        for num in nums:
            running_sum = max(running_sum + num,num)
            max_sum = max(max_sum,running_sum)
        
        return max_sum