class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output=[]
        num=''
        
        
        for i in digits:
            num+=str(i)
        num=str(int(num)+1)
        for i in num:
            output.append(int(i))
        return output