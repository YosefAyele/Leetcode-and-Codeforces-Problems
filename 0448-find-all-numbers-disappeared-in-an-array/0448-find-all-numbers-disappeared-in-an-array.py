class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0
        
        while i < n:
            curr = nums[i] - 1
            
            if curr >= n:
                nums[i] = -1
            elif curr != i and nums[i] != nums[curr]:
                nums[curr] , nums[i] = nums[i], nums[curr]
            else:
                i += 1
        res = []
        
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        
        return res