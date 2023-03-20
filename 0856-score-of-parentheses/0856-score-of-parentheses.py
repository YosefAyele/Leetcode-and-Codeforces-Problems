class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        res = 0
        
        stack = [0]
        
        for bracket in s:
            
            if bracket == "(":
                stack.append(0)
                
            else:
                
                last = stack.pop()
                prevLast = stack.pop()
                
                stack.append(prevLast + max(last*2,1))
                
        return stack[-1]