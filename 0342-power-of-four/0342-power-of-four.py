class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        def recur(num):
            
            if num == 1:
                return True
            if num < 1 or num % 4:
                return False
    
            
            return recur(num//4)
        
        
        return recur(n)
    
    