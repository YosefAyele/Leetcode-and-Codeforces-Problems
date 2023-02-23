class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = list(accumulate(nums))
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = self.prefixSum[right] - self.prefixSum[left] + self.nums[left]
        
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)