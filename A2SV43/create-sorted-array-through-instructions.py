class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        
        sorted_arr = []
        
        ans = 0
        for i, num in enumerate(A):
            l, r = bisect.bisect_left(sorted_arr, num), bisect.bisect_right(sorted_arr, num)
            
            ans += min(l, i-r)
            sorted_arr[r:r] = [num]
         
        return ans % (10**9 + 7) 
            
            
            