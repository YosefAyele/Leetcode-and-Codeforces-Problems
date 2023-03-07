class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def findLeftMost():
        
            left, right = 0, n-1
            best = -1
            
            while left <= right:
                mid = (left + right)//2
                
                if nums[mid] >= target:
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return best
        
        def findRightMost():
            left, right = 0, n-1
            best = -1
            
            while left <= right:
                mid = (left + right)//2
                
                if nums[mid] <= target:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return best
        
        
        left, right = findLeftMost(), findRightMost()
        
        if left < 0 or right < 0: return [-1, -1]
        if nums[left] != target or (right < len(nums) and nums[right] != target): return [-1, -1]
        
        return [left, right]
        
                    
        
        