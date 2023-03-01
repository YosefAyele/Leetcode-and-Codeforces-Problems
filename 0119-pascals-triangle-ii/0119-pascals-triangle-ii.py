class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [[1]]
        
        def pascal(arr,n):
            
            if n == 0:
                return 
            
            temp = [0] + arr[-1] + [0]
            curr = []
            
            for i in range(len(temp)-1):
                
                curr.append(temp[i]+temp[i+1])
            
            arr.append(curr)
            
            pascal(arr,n-1)
        
        pascal(res,rowIndex)
        
        return res[rowIndex]
            
            
        
            

            
            