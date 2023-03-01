class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = (1/x)
            n = -n
        
        def power(n,res):
            
            if n == 0:
                return 1
            
            return res*power(n//2,res*res) if n%2 else power(n//2,res*res)
            
            

        
        
        return power(n,x)