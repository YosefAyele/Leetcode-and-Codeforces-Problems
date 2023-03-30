class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        
        def backtrack(idx,curr):
            
            if len(curr) == len(nums):
                res.add(tuple(curr[:]))
                return
            
            for i in range(len(nums)):
                
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(i,curr)
                    curr.pop()

            
        for idx in range(len(nums)):
            backtrack(idx,[])
        
        return res