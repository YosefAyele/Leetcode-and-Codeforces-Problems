class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {"+","-","*","/"}
        res= []
        for token in tokens:
            
            if token in operators:
                num2 = int(res.pop())
                num1 = int(res.pop())
                
                if token == "+":
                    evaluatedValue = num1 + num2
                elif token == "-":
                    evaluatedValue = num1 - num2
                elif token == "*":
                    evaluatedValue = num1 * num2
                else:
                    evaluatedValue = num1 / num2
                
                res.append(int(evaluatedValue))
            else:
                res.append(int(token))
        
        return res[0]
                