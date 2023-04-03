class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def GCD(a,b):
            
            if not b:
                return a
            return GCD(b,a%b)
        
        return GCD(max(nums),min(nums))