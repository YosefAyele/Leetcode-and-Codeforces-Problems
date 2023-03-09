class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        mega = []
        
        
        def getCombinations(currVal,currList,maxIdx,k):
            
            
            if len(currList) == k:
                mega.append(currList[:])
                return
            if currVal > n:
                return 
            
            # case1: Not Include the current
            getCombinations(currVal+1,currList,maxIdx,k)
            
            
            # case2: Include the current
            currList.append(currVal)
            getCombinations(currVal+1,currList,maxIdx,k)
            
            currList.pop()
          
        
        
        getCombinations(1,[],n,k)
        
        
        return mega
        