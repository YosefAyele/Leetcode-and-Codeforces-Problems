class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        i = 2
        
        while i*i < n:
            
            if isPrime[i]:
                
                j = i*i


                while j < n:
                    if isPrime[j]:
                        isPrime[j] = False
                    j += i

            if i == 2:
                i += 1
            else:
                i += 2
    
        return Counter(isPrime)[True]
        
        
            
        