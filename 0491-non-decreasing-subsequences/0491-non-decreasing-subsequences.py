class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # nums.sort()
        seen = set()
        def backtrack(idx,curr):
            nonlocal res
            nonlocal seen
            if idx == len(nums):
                if len(curr) > 1 and tuple(curr) not in seen:
                    res.append(curr[:])
                    seen.add(tuple(curr[:]))
                return 
           
            
            # case1 not include the current number
            i = idx + 1
            backtrack(i,curr)
            
            if curr and  curr[-1] > nums[idx]:
                return 
            
            # case2 : include current
            curr.append(nums[idx])
            backtrack(idx+1,curr)
            curr.pop()
            return 
        
        
        backtrack(0,[])
        
        return res