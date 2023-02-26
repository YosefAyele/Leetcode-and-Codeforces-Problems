class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumCount = {0:1}
        
        res = 0
        runningSum = 0
        for i,num in enumerate(nums):
            
            runningSum += num
            
            if runningSum - k in sumCount:
                res += sumCount[runningSum - k]
            
            sumCount[runningSum] = sumCount.get(runningSum,0) + 1
        
        
        return res