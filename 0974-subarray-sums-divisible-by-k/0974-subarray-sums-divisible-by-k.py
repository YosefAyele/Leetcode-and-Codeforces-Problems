class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        runningSum = 0
        modCount = {0:1}
        res = 0
        for i,num in enumerate(nums):
            
            runningSum += num
            
            if runningSum % k in modCount:
                res += modCount[runningSum%k]
            
            modCount[runningSum%k] = modCount.get(runningSum%k,0) + 1
        
        return res
                