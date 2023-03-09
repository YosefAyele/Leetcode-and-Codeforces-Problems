class Solution:
    def splitString(self, s: str) -> bool:
        
        
        
        def split(idx,last):
            
            # print(idx, last)
            if idx == len(s):
                
                return True

            temp = False
            for end in range(idx+1,len(s)+1):
                currNum = int(s[idx:end])
                
                if last - currNum == 1:
                    
                    temp = temp or split(end,currNum)
            
            return temp
        
        ans = False
        for end in range(1, len(s)):
            
            ans =  ans or split(end,int(s[:end]))
        
        
        return ans
        
        