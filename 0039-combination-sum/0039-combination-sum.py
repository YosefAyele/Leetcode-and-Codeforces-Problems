class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx,curr,sum_):
            
            if idx == len(candidates) or sum_ >= target:
                if sum_ == target:
                    res.append(curr)
                return
            
            # not include
            backtrack(idx+1,curr,sum_)
            
            # include
            curNum = candidates[idx]
            freq = (target - sum_)//curNum
            
            for i in range(1,freq+1):
                backtrack(idx+1,curr + [curNum]*i, sum_ + i*curNum)
                
        backtrack(0,[],0)
        
        return res
            
    