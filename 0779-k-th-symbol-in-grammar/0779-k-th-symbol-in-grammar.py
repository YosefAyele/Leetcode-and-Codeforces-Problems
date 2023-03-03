class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        k -= 1
        def getBit(n,k):
            
            if n == 1:
                return 0

            prevLength = 2**(n-2)
            
            if k >= prevLength:
                # print(2323)
                return 1 - getBit(n-1, k%prevLength)
            else:
                return getBit(n-1, k%prevLength)
        
        
        return getBit(n,k)