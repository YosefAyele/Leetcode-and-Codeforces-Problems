class Solution:
    def decodeString(self, s: str) -> str:
        
        res = []
        curr = ''
        def decode(right):
            nonlocal res
            nonlocal curr
            
            i = 1
            k = 0
            
            if right == len(s):
                return
            if s[right] == "]":
                
                while res and res[-1] != "[":
                    
                    curr = res.pop() + curr
                res.pop()
                
                while res and res[-1].isnumeric():
                    
                    k += int(res.pop()) * i
                    i *= 10
                res.append(k*curr)
                curr = ""
            else:
                res.append(s[right])
            
            decode(right+1)
        
        decode(0)
        
        
        ans = "".join(res)
        
        if ans.isnumeric():
            return ""
        return ans
                    
        