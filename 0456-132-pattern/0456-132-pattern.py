class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        monStack = []
        
        second = -math.inf
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            if num < second:
                return True
            
            while monStack and num > monStack[-1]:
                second = monStack.pop()
                
            monStack.append(num)
            
        
        return False
    
    
      