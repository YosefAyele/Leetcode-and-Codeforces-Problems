class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def recur(num):
            
            if num < 1:
                return False
            if num == 1:
                return True
            
            if num % 4 != 0:
                return False
         
            if num < 4 and num > 1:
                return False
            return recur(num//4)
        
        
        return recur(n)
    
    