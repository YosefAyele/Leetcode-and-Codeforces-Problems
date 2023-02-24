class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = {i:-1 for i in range(n)}
        
        monStack = []
        
        for i in range(2*n):
            
            while monStack and nums[i%n] > nums[monStack[-1]]:
                       res[monStack.pop()] = nums[i%n]
            
            monStack.append(i%n)
        
        return [res[i] for i in range(n)]