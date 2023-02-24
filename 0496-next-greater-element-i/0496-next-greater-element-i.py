class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = {num:-1 for num in nums2}
        monStack = []
        
        for i,num in enumerate(nums2):
            
            while monStack and num > monStack[-1]:
                res[monStack.pop()] = num
            
            monStack.append(num)
        return [res[num] for num in nums1]
            