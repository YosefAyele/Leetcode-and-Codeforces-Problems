class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = list(accumulate(nums))
        
        for i,num in enumerate(nums):
            
            if prefix[i] - nums[i] == prefix[-1] - prefix[i]:
                return i
        
        return -1
        