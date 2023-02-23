class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num%2 for num in nums]
        
        curr = 0 
        
        left = 0
        
#         exactly k = atmost k - atmost k-1
        atmostK = 0
        atmostKless1 = 0
        for right,num in enumerate(nums):
            
            curr += num
            
            while curr > k:
                curr -= nums[left]
                left += 1
            atmostK += (right - left + 1)
        
        left = 0
        newCurr = 0 
        for right,num in enumerate(nums):
            
            newCurr += num
            
            while newCurr > k - 1:
                newCurr-= nums[left]
                left += 1
            atmostKless1 += (right - left + 1)        
    
        return atmostK - atmostKless1
            
            