class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        productBefore = []
        
        # building product of arrays before each element
        proBefore = 1
        
        for i,num in enumerate(nums):
            productBefore.append(proBefore)
            proBefore *= num
        
        productAfter = [0]*len(nums)
        
        proAfter = 1
        
        # building product of Arrays after each element
        
        for i in range(len(nums)-1,-1,-1):
            productAfter[i] = proAfter
            
            proAfter *= nums[i]
        
        
        return [productAfter[i]*productBefore[i] for i in range(len(nums))]