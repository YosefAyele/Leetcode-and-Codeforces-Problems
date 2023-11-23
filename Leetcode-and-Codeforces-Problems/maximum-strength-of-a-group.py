class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = []
        neg = []
        
        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(abs(num))

        neg.sort(reverse = True)

        if len(neg) % 2:
            neg.pop()

        if not pos and not neg:
            return 0

        return prod(pos) * prod(neg)
        

        



        