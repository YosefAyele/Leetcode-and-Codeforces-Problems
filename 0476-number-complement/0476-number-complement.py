class Solution:
    def findComplement(self, num: int) -> int:
        
        n = int(log(num,2))
        
        if 1 >> n == num:
            return num - 1
        
        mask = ( 1 << (n+1)) - 1
    
        return num ^ mask