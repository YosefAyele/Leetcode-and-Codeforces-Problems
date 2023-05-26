class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        # solution2
        res = 0
        running_sum = 0
        
        for i,num in enumerate(nums):
            running_sum += num
            curr = ceil(running_sum/(i+1))
            res = max(res,curr)
        
        return res