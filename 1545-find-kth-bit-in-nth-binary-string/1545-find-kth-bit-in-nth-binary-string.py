class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = "0"
        # print(str(int(not int(s1))))
        
        def getBinary(s,n):
            
            if n == 0:
                return s
            invertedS = [str(int(not int(bit))) for bit in s]
            reversedInvertedS = "".join(invertedS[::-1])
            newStringBit = s + "1" + reversedInvertedS
            
            return getBinary(newStringBit,n-1)
        Sth = getBinary(s,n)
        
        return Sth[k-1]
        