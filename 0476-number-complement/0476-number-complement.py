class Solution:
    def findComplement(self, num: int) -> int:
        
        mask = 1
        
        while mask <= num:
            num ^= mask
            mask <<= 1
            
            
        return num