class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prevMin = {}
        nextMin = {}
        
        mins = []
        
        res = 0
        for i, num in enumerate(arr):
            
            while mins and num <= arr[mins[-1]]:
                nextMin[mins.pop()] = i 
            
            if mins:
                prevMin[i] = mins[-1] 
            else:
                prevMin[i] = -1
            mins.append(i)
        for i in mins:
            nextMin[i] = len(arr) 
            
            
        for i in range(len(arr)):
            
            res += (nextMin[i] - i)*(i-prevMin[i])*arr[i]
        
        
        
        return res%(10**9 + 7)