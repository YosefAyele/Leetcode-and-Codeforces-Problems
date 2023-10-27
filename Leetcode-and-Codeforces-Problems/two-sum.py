class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {num:i for i,num in enumerate(nums)}

        for i,num in enumerate(nums):
            if target - num in dictionary and i != dictionary[target - num]:
                return i,dictionary[target-num]
        
        