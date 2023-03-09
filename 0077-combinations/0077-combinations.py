class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        mega = []
        
        
        def getCombinations(currVal,currList,maxIdx,k):
            currList.append(currVal)
            
            if len(currList) == k:
                mega.append(currList)
                return
            
            
            for j in range(currVal+1,maxIdx+1):
                getCombinations(j,[num for num in currList],maxIdx,k)
        
        for i in range(1,n+1):
            getCombinations(i,[],n,k)
        
        
        return mega
        