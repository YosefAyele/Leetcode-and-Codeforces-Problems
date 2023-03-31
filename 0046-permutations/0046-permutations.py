class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(curr,mask):
            
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                
                if (1 << i) & mask:
                    curr.append(nums[i])
                    mask ^= (1 << i)
                    
                    backtrack(curr,mask)
                    curr.pop()
                    mask |= (1 << i)
                    
        mask = (1 << len(nums)) - 1
        backtrack([],mask)
        
        return res
            