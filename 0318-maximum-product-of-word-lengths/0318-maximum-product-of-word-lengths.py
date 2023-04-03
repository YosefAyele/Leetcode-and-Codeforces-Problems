class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def getBit(s):
            res = (1 << 26) ^ (1 << 26)
            for c in s:
                mask = 1
                pos = ord(c) - 97
                mask <<= pos
                res |= mask
            return res
        
        
        res = 0
        binArr = [getBit(word) for word in words]
        for i,wordBit in enumerate(binArr):
            for j in range(i+1,len(words)):
                if not (wordBit & binArr[j]):
                    res = max(res,len(words[i])*len(words[j]))
                    
        return res