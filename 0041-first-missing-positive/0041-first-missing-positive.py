class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        for num in nums:
            if 0 <= abs(num) - 1 < len(nums):
                if nums[abs(num) - 1] > 0:
                    nums[abs(num) - 1] = - nums[(abs(num) - 1)]
                elif nums[abs(num) - 1] == 0:
                    nums[abs(num) - 1] = -(len(nums) + 1)
        smallest = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                smallest += 1
            else:
                return smallest
        
        return smallest
            
            
                