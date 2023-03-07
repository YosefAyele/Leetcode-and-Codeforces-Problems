class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def findLeftMost():
        
            left, right = -1, n
            # best = -1
            
            while right > left + 1:
                mid = (left + right)//2
                
                if nums[mid] >= target:
                    
                    right = mid 
                else:
                    left = mid 
            
            return right
        
        def findRightMost():
            left, right = -1, n
            best = -1
            
            while right > left + 1:
                mid = (left + right)//2
                
                if nums[mid] <= target:
                    
                    left = mid
                else:
                    right = mid 
            
            return left
        
        
        left, right = findLeftMost(), findRightMost()
        print(left,right)
        if left < 0 or right < 0 or right >= len(nums) or left >= len(nums): return [-1, -1]
        if nums[left] != target or nums[right] != target: return [-1, -1]
        
        return [left, right]
        
                    
        
        