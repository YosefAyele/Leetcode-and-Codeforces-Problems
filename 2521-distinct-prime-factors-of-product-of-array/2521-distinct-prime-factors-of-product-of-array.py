class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        
        factors = set()
        def getFactors(n):
            
            factor = 2

            while factor * factor <= n:

                while not n % factor:
                    factors.add(factor)
                    n //= factor

                factor += 1
            if n > 1:
                factors.add(n)
                
        for num in nums:
            getFactors(num)
            

        return len(factors)
        