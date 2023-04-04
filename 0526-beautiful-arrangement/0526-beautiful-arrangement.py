class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        def backtrack(curr,mask):
            nonlocal res
            if len(curr) == n:
                res += 1
                return 
            for i in range(n):
                if mask & (1<<i):
                    idx = len(curr) + 1
                    if idx % (i+1) and (i+1)%idx:
                        continue
                    curr.append(i+1)
                    
                    mask ^= (1 << i)
                    
                    backtrack(curr,mask)
                    curr.pop()
                    mask |= (1 << i)
                    
        mask = (1 << n) - 1    
        backtrack([],mask)
        
        return res
                    
                    
                