class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        nums = list(counts.items())
        
        nums.sort(reverse = True, key = lambda x:x[1])
        
        return [nums[i][0] for i in range(k)]