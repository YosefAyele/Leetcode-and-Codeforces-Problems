class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        
        def GCD(a,b):
            if not b:
                return a
            return GCD(b,a%b)
        res = 0
        for i in range(len(nums)):
            curr = nums[i]
            
            for j in range(i,len(nums)):
                curr = GCD(curr,nums[j])
            
                if curr == k:
                    res += 1
                elif curr < k or  nums[j]%k != 0:

                    break
        return res