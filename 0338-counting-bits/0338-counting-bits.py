class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0]
        most_bit = 1
        
        for i in range(1,n+1):
            
            if i & most_bit << 1:
                most_bit <<= 1
                
            inner = i - most_bit
            res.append(res[inner] + 1)
        
        return res