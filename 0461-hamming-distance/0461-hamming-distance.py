class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        num = x ^ y
        mask = 1
        res = 0
        while mask <= num:
            if num & mask:
                res += 1
            mask <<= 1
        
        return res