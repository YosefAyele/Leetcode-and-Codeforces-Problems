class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        res = []
        
        def backtrack(i,dots):
            
            if len(dots) > 4:
                return 
            if len(dots) == 4 and i >= len(s):
                curr = s[:dots[0]+1] + "." + s[dots[0]+1:dots[1]+1] + "." + s[dots[1]+1:dots[2]+1] + "." + s[dots[2]+1:]
                res.append(curr)
                return
   
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1]) < 256 and (len(s[i:j+1]) == 1 or s[i] != "0"):
                
                    dots.append(j)
                    backtrack(j+1,dots)
                    dots.pop()
                    
        backtrack(0,[])
        
        return res
                
                