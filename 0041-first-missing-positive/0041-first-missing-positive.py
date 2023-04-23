class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        positives = set()
        
        for num in nums:
            if num > 0:
                positives.add(num)
        
        for num in range(1,10**5 + 2):
            if num not in positives:
                return num