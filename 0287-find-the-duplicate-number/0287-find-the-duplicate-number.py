class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        
        while i < n:
            curr = nums[i] - 1
            
            if curr != i and nums[curr] != nums[i]:
                nums[curr], nums[i] = nums[i], nums[curr]
            else:
                i += 1
        
        
        
        for i in range(n):
            
            if nums[i] != i + 1:
                
                return nums[i]