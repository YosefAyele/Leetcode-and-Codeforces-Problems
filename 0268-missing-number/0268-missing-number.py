class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append(-1)
        
        for i in range(2*len(nums)):
            i %= len(nums)
            num = nums[i]
            
            while num != i and num != -1:
                nums[i], nums[num] = nums[num], nums[i]
                num = nums[i]
                    
        
        # print(nums)
        for i in range(len(nums)):
            if nums[i] == -1:
                return i