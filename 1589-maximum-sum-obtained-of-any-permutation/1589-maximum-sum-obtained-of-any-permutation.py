class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        
        requestFreq = [0]*(len(nums)+1)
        
        
        
        for start, end in requests:
            
            requestFreq[start] += 1
            requestFreq[end + 1] -= 1
            
        
        
        
        requestFreq = list(accumulate(requestFreq))
        freqIdx = [(requestFreq[i],i) for i in range(len(nums))]
        
        freqIdx.sort(reverse=True)
        nums.sort(reverse=True)
        
        best = [0] * len(nums)
        for i,num in enumerate(nums):
            
            best[freqIdx[i][1]] = num
        
        bestSum = list(accumulate(best))
        
        res = 0
        
        for start,end in requests:
            
            curr = bestSum[end] - bestSum[start] + best[start]
            
            res += curr
        
        
        return res %(10**9 + 7)
            
            
        
        
            