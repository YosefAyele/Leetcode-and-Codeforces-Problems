class Solution:
    def findComplement(self, num: int) -> int:
        
        mask = 1
        
        while mask < (num << 1):
            num ^= mask
            mask <<= 1
            
            
        return num