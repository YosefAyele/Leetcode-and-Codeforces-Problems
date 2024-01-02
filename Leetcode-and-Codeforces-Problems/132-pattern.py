class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        prefixmin = [-1]*len(nums)
        prefixmin[0] = nums[0]
        for i in range(1,len(nums)):
            prefixmin[i] = min(nums[i],prefixmin[i-1])

        stack = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > prefixmin[i]:

                while stack and stack[-1] <= prefixmin[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True

                stack.append(nums[i])
        
        return False
               