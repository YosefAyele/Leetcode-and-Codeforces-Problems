class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # space optimized bottom up dp
        # need to check when starting from 1 and when starting from 2 so two for loops
        n = len(nums)
        if n <= 2:
            return max(nums)
        x1 = nums[0]
        y1 = max(nums[0],nums[1])
        
        # since I might have taken the first I should avoid using the last element
        for i in range(2,n-1):
            curr = max(nums[i] + x1,y1)
            x1 = y1
            y1 = curr
        
        x2 = nums[1]
        y2 = max(nums[1],nums[2])
        
        for i in range(3,n):
            curr = max(nums[i] + x2,y2)
            x2 = y2
            y2 = curr
            
        return max(y1,y2)
            