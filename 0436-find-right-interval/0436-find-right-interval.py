class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        indexes = {intervals[i][0]:i for i in range(len(intervals))}
        
        newIntervals = sorted(indexes)
        # print(newIntervals)
        
        def search(target):
            
            low = -1
            high = len(intervals)
            
            while high > low + 1:
                
                mid = low + (high - low)//2
                
                if newIntervals[mid] < target:
                    low = mid
                else:
                    high = mid
            # print(high) 
            if high < len(intervals):
                start = newIntervals[high]
                return indexes[start]
            else:
                return -1
        res = []
        
        for start,end in intervals:
            
            res.append(search(end))
        
        return res
        
         
            
        
        
                    
                    