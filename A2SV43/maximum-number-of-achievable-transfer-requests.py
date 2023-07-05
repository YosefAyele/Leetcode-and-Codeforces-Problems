class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        res = 0
        def backtrack(idx,curr,reqs):
            
            nonlocal res
            if idx == len(requests):
                if len(set(curr)) == 1 and curr[0] == 0:
                    res = max(res,reqs)
                return
            f, t = requests[idx]
            # not_take 
            backtrack(idx + 1, curr,reqs)
            
            # take
            curr[f] -= 1
            curr[t] += 1
            backtrack(idx + 1,curr,reqs + 1)
            
            curr[f] += 1
            curr[t] -= 1
            
        backtrack(0,[0]*n,0)
        
        return res
            
            
            
        