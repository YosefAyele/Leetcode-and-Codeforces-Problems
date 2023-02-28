class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def recur(num): 
            if num == 1:
                return True
            if num%3 or num < 1:
                return False
            
            return recur(num//3)
        
        return recur(n)
    
        
        