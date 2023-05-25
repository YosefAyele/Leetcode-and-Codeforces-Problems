class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        max_ = 1
        arr[0] = 1
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] >= 1:
                arr[i] = max_ + 1
                max_ += 1
            
        return max_
                
            
            
        