class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        maxOr = 0
        for num in nums:
            maxOr |= num
        
        def backtrack(idx,curr,currOr):
            nonlocal maxOr, res
            if idx == len(nums):
                return
            
            # not include
            backtrack(idx+1,curr,currOr)
            
            # include
            save = currOr
            currOr |= nums[idx]
            curr.append(currOr)
            
            if currOr == maxOr:
                res += 1
            
            backtrack(idx+1,curr,currOr)
            curr.pop()
            currOr = save
        
        backtrack(0,[],0)
        
        return res
            
                    