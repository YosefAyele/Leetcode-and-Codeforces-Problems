class Solution:
    def splitString(self, s: str) -> bool:
        
        
        
        def split(idx,last):
            
            
            if idx == len(s):
                return True

            
            for end in range(idx+1,len(s)+1):
                currNum = int(s[idx:end])
                
                if last - currNum == 1:
                    
                    if split(end,currNum):
                        return True
            
            return False
        
        ans = False
        for start in range(1, len(s)):
            
            ans =  ans or split(start,int(s[:start]))
            if ans:
                return True
        
        
        return ans
        
        