class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        
        requestFreq = [0]*(len(nums)+1)
        res = 0
        
        
        for start, end in requests:
            
            requestFreq[start] += 1
            requestFreq[end + 1] -= 1
            
        
        
        
        requestFreq = list(accumulate(requestFreq))
        requestFreq.sort(reverse=True)
        nums.sort(reverse = True)
        
        for i in range(len(nums)):
            
            res += requestFreq[i]*nums[i]
        
        
        return res %(10**9 + 7)
            
            
        
        
            