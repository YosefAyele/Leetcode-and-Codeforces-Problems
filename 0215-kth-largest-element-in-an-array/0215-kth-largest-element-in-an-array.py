class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #bucket sort
        
        bucket = [0]* (2*(10**4 )+ 1)
        counts = Counter(nums)
        # print(counts)
        
        
        for idx in range(len(bucket)-1, -1, -1):
            k -= counts[idx - 10**4]
            
            if k <= 0:
                return idx - 10**4
            
        