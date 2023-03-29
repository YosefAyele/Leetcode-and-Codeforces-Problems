class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        
        for i in range(n+1):
            
            curr = 0
            while i:
                curr += i&1
                i >>= 1
            res.append(curr)
        
        return res