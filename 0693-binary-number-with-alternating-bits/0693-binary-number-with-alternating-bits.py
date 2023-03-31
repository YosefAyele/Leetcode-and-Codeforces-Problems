class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        mask = 1
        isOne = 0
        isZero = 0
        while mask <= n:
            
            if n & mask:
                isOne += 1
                isZero = 0
                
                if isOne > 1:
                    return False
            else:
                isZero += 1
                isOne = 0
                
                if isZero > 1:
                    return False
            mask <<= 1
            
        return True