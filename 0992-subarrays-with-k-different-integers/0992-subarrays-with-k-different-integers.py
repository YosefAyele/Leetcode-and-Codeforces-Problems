class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        curr = {}
        
        left = 0
        
#         exactly k = atmost k - atmost k-1
        atmostK = 0
        atmostKless1 = 0
        for right,letter in enumerate(nums):
            
            curr[letter] = curr.get(letter,0) + 1
            
            while len(curr) > k:
                curr[nums[left]] -= 1
                if curr[nums[left]] == 0:
                    del curr[nums[left]]
                left += 1
            atmostK += (right - left + 1)
        
        left = 0
        newCurr = {}
        for right,letter in enumerate(nums):
            
            newCurr[letter] = newCurr.get(letter,0) + 1
            
            while len(newCurr) > k - 1:
                newCurr[nums[left]] -= 1
                if newCurr[nums[left]] == 0:
                    del newCurr[nums[left]]
                left += 1
            atmostKless1 += (right - left + 1)        
    
        return atmostK - atmostKless1