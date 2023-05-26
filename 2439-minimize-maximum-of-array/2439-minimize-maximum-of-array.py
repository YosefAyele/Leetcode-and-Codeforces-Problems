class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        def check(num):
            curr = nums[-1]
            
            for i in range(len(nums)-1,0,-1):
                if curr > num:
                    curr = nums[i-1] + curr - num
                else:
                    curr = nums[i-1]
            return curr
        high = low = nums[0]
        
        for num in nums:
            high = max(high,num)
            low  = min(low,num)
        
        low -= 1
        high += 1
        
        while high > low + 1:
            mid = low + (high-low)//2
            curr = check(mid)
            # print(mid,curr)
            if curr > mid:
                low = mid
            else:
                high = mid
                
        return high