class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
    
        
        nums.sort()
        
        ans = inf
        print(nums)
        
        j = len(nums) - 4
        
        for i in range(4):
            ans = min(ans,nums[j]-nums[i])
            j += 1

        return ans

   
    
            
        