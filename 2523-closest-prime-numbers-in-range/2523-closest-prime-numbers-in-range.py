class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        isPrime = [True] * (right + 1)
        isPrime[0] = isPrime[1] = False
        
        i = 2
        while i < len(isPrime):
            
            if isPrime[i]:
                j = i * i
                
                while j < len(isPrime):
                    isPrime[j] = False
                    j += i
            if i == 2:
                i += 1
            else:
                i += 2
                
        prev = -1
        curr = -1
        
        res = []
        
        for num in range(left,right+1):
            
            if isPrime[num]:
                
                prev = curr
                curr = num
                
                if not res:
                    res = [prev,curr]
    
                elif curr - prev < res[1] - res[0]:
                    res = [prev,curr]
                
    
        if not res or res[0] == -1 or res[1] == -1:
            return [-1,-1]
        return res
                    